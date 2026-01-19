from json import load

from buttonlayout import ButtonLayout
from game import Game
from hint import Hint

class DonkeyKong64BatchesSeason4(Game):

    def __init__(self):
        super().__init__()

    def getGameNameText(self) -> str:
        return "Donkey Kong 64 (Season 4, Batch Hints)"

    def getHintList(self) -> list[Hint]:
        return [
            Hint(['Japes DK', 'Japes Diddy', 'Japes Lanky', 'Japes Tiny'], None, 'Batch 1'),
            Hint(['Japes Chunky', 'Aztec DK', 'Aztec Diddy', 'Aztec Lanky'], None, 'Batch 2'),
            Hint(['Aztec Tiny', 'Aztec Chunky', 'Factory DK', 'Factory Diddy'], None, 'Batch 3'),
            Hint(['Factory Lanky', 'Factory Tiny', 'Factory Chunky', 'Galleon DK'], None, 'Batch 4'),
            Hint(['Galleon Diddy', 'Galleon Lanky', 'Galleon Tiny', 'Galleon Chunky'], None, 'Batch 5'),
            Hint(['Fungi DK', 'Fungi Diddy', 'Fungi Lanky', 'Fungi Tiny'], None, 'Batch 6'),
            Hint(['Fungi Chunky', 'Caves DK', 'Caves Diddy', 'Caves Lanky'], None, 'Batch 7'),
            Hint(['Caves Tiny', 'Caves Chunky', 'Castle DK', 'Castle Diddy'], None, 'Batch 8'),
            Hint(['Castle Lanky', 'Castle Tiny'], None, 'Batch 9'),
            Hint(['Castle Chunky'], None, 'Batch 10'),
            Hint(['Bongos'], '/supportedGames/dk64/images/bongos.png', 'Bongos Hint'),
            Hint(['Guitar'], '/supportedGames/dk64/images/guitar.png', 'Guitar Hint'),
            Hint(['Trombone'], '/supportedGames/dk64/images/trombone.png', 'Trombone Hint'),
            Hint(['Saxophone'], '/supportedGames/dk64/images/saxophone.png', 'Saxophone Hint'),
            Hint(['Triangle'], '/supportedGames/dk64/images/triangle.png', 'Triangle Hint'),
            Hint(['Candy'], '/supportedGames/dk64/images/candy.png', 'Candy Kong Hint'),
            Hint(['Cranky'], '/supportedGames/dk64/images/cranky.png', 'Cranky Kong Hint'),
            Hint(['Funky'], '/supportedGames/dk64/images/funky.png', 'Funky Kong Hint'),
            Hint(['Snide'], '/supportedGames/dk64/images/snide.png', 'Snide Hint'),
            Hint(['Monkeyport'], '/supportedGames/dk64/images/monkeyport.png', 'Monkeyport Hint'),
            Hint(['Progressive Slam'], '/supportedGames/dk64/images/progressiveslam.png', 'Progressive Slam Hint')
        ]

    def readFromSpoilerLog(self, f) -> dict:
        with open(f, encoding='utf-8-sig') as myFile:
            data = load(myFile)
        allHints = dict()
        directItemHints = dict(data['Direct Item Hints'].items())
        wrinklyItemHints = dict(data['Wrinkly Hints'].items())
        for hint in directItemHints.items():
            allHints[hint[0]] = self.sanitizeHint(hint)
        for hint in wrinklyItemHints.items():
            if hint[0] == 'First Time Talk':
                continue
            allHints[hint[0]] = self.sanitizeHint(hint)
        result = {k: v for k, v in allHints.items()}
        return result

    def sanitizeHint(self, hint):
        return hint[1].replace("YOU WOULD BE BETTER OFF LOOKING FOR SHOPS IN", "Look for shops in") \
            .replace("Something about collecting", "Collecting") \
            .replace("YOU WOULD BE BETTER OFF LOOKING FOR", "Look for") \
            .replace("YOU WOULD BE BETTER OFF LOOKING IN", "Look in") \
            .replace("ANY KONG", "any Kong") \
            .replace("LADIES AND GENTLEMEN! IT APPEARS THAT ONE FIGHTER HAS COME UNEQUIPPED TO PROPERLY HANDLE THIS REPTILIAN BEAST. PERHAPS THEY SHOULD HAVE LOOKED", "Look") \
            .replace("Still looking for some super slam strength? Try looking in", "Slam upgrades can be found in") \
            .replace("Final ", "") \
            .replace("FOR THE ELUSIVE SLAM.", "for the elusive Slam.") \
            .replace("A FAIRY", "a fairy") \
            .replace("A BATTLE CROWN", "a battle crown") \
            .replace("A DIRT PATCH", "a dirt patch") \
            .replace("A BATTLE ARENA", "a Battle Arena") \
            .replace("A KASPLAT", "a Kasplat") \
            .replace("A MELON CRATE", "a melon crate") \
            .replace("JUNGLE JAPES", "Jungle Japes") \
            .replace("ANGRY AZTEC", "Angry Aztec") \
            .replace("FRANTIC FACTORY", "Frantic Factory") \
            .replace("GLOOMY GALLEON", "Gloomy Galleon") \
            .replace("FUNGI FOREST", "Fungi Forest") \
            .replace("CRYSTAL CAVES", "Crystal Caves") \
            .replace("CREEPY CASTLE", "Creepy Castle") \
            .replace("HIDEOUT HELM", "Hideout Helm") \
            .replace("DK ISLES", "DK Isles") \
            .replace("CRANKY'S LAB", "Cranky's Lab") \
            .replace("DONKEY", "Donkey") \
            .replace("DIDDY", "Diddy") \
            .replace("TINY", "Tiny") \
            .replace("LANKY", "Lanky") \
            .replace("CHUNKY", "Chunky") \
            .replace("FOR A", "for a") \
            .replace("IN", "in") \
            .replace("WITH", "with") \
            .replace("FOR THIS.", "for this: " + hint[0] + ".") \
            .replace("OR", "or") \
            .replace("Something in the ", "") \
            .replace("CANDY", "Candy") \
            .replace("FUNKY", "Funky") \
            .replace("CRANKY", "Cranky") \
            .replace("HAS GONE ON VACATION TO THE UNDENIABLE SERENITY OF", "can be found in") \
            .replace("HAS GONE ON VACATION TO THE OSHA VIOLATION HOTSPOT OF", "can be found in") \
            .replace("this: Monkeyport", "Monkeyport") \
            .replace("this: Guitar", "the Guitar") \
            .replace("this: Trombone", "the Trombone") \
            .replace("this: Triangle", "the Triangle") \
            .replace("this: Gorilla Gone", "Gorilla Gone") \
            .replace("this: Bongos", "the Bongos") \
            .replace("this: Saxophone", "the Saxophone")

    def getMaxButtonsPerColumn(self) -> int:
        return 5

    def getButtonWidth(self) -> int:
        return 64

    def getButtonHeight(self) -> int:
        return 64

    def getButtonLayout(self) -> list[ButtonLayout]:
        return [
            ButtonLayout('Batches', 10),
            ButtonLayout('Instruments', 5),
            ButtonLayout('Shops', 4),
            ButtonLayout('Other', 2)
        ]

    def isRowBasedLayout(self) -> bool:
        return False

    def getWidthGapBetweenButtons(self) -> int:
        return 10
