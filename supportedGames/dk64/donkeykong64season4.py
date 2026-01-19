from json import load

from buttonlayout import ButtonLayout
from game import Game
from hint import Hint

class DonkeyKong64Season4(Game):

    def __init__(self):
        super().__init__()

    def getGameNameText(self) -> str:
        return "Donkey Kong 64 (Season 4, Wrinkly Hints)"

    def getHintList(self) -> list[Hint]:
        return [
            Hint(['Japes DK'], '/supportedGames/dk64/images/dk.png', 'Jungle Japes - DK Hint'),
            Hint(['Japes Diddy'], '/supportedGames/dk64/images/diddy.png', 'Jungle Japes - Diddy Hint'),
            Hint(['Japes Lanky'], '/supportedGames/dk64/images/lanky.png', 'Jungle Japes - Lanky Hint'),
            Hint(['Japes Tiny'], '/supportedGames/dk64/images/tiny.png', 'Jungle Japes - Tiny Hint'),
            Hint(['Japes Chunky'], '/supportedGames/dk64/images/chunky.png', 'Jungle Japes - Chunky Hint'),
            Hint(['Aztec DK'], '/supportedGames/dk64/images/dk.png', 'Angry Aztec - DK Hint'),
            Hint(['Aztec Diddy'], '/supportedGames/dk64/images/diddy.png', 'Angry Aztec - Diddy Hint'),
            Hint(['Aztec Lanky'], '/supportedGames/dk64/images/lanky.png', 'Angry Aztec - Lanky Hint'),
            Hint(['Aztec Tiny'], '/supportedGames/dk64/images/tiny.png', 'Angry Aztec - Tiny Hint'),
            Hint(['Aztec Chunky'], '/supportedGames/dk64/images/chunky.png', 'Angry Aztec - Chunky Hint'),
            Hint(['Factory DK'], '/supportedGames/dk64/images/dk.png', 'Frantic Factory - DK Hint'),
            Hint(['Factory Diddy'], '/supportedGames/dk64/images/diddy.png', 'Frantic Factory - Diddy Hint'),
            Hint(['Factory Lanky'], '/supportedGames/dk64/images/lanky.png', 'Frantic Factory - Lanky Hint'),
            Hint(['Factory Tiny'], '/supportedGames/dk64/images/tiny.png', 'Frantic Factory - Tiny Hint'),
            Hint(['Factory Chunky'], '/supportedGames/dk64/images/chunky.png', 'Frantic Factory - Chunky Hint'),
            Hint(['Galleon DK'], '/supportedGames/dk64/images/dk.png', 'Gloomy Galleon - DK Hint'),
            Hint(['Galleon Diddy'], '/supportedGames/dk64/images/diddy.png', 'Gloomy Galleon - Diddy Hint'),
            Hint(['Galleon Lanky'], '/supportedGames/dk64/images/lanky.png', 'Gloomy Galleon - Lanky Hint'),
            Hint(['Galleon Tiny'], '/supportedGames/dk64/images/tiny.png', 'Gloomy Galleon - Tiny Hint'),
            Hint(['Galleon Chunky'], '/supportedGames/dk64/images/chunky.png', 'Gloomy Galleon - Chunky Hint'),
            Hint(['Fungi DK'], '/supportedGames/dk64/images/dk.png', 'Fungi Forest - DK Hint'),
            Hint(['Fungi Diddy'], '/supportedGames/dk64/images/diddy.png', 'Fungi Forest - Diddy Hint'),
            Hint(['Fungi Lanky'], '/supportedGames/dk64/images/lanky.png', 'Fungi Forest - Lanky Hint'),
            Hint(['Fungi Tiny'], '/supportedGames/dk64/images/tiny.png', 'Fungi Forest - Tiny Hint'),
            Hint(['Fungi Chunky'], '/supportedGames/dk64/images/chunky.png', 'Fungi Forest - Chunky Hint'),
            Hint(['Caves DK'], '/supportedGames/dk64/images/dk.png', 'Crystal Caves - DK Hint'),
            Hint(['Caves Diddy'], '/supportedGames/dk64/images/diddy.png', 'Crystal Caves - Diddy Hint'),
            Hint(['Caves Lanky'], '/supportedGames/dk64/images/lanky.png', 'Crystal Caves - Lanky Hint'),
            Hint(['Caves Tiny'], '/supportedGames/dk64/images/tiny.png', 'Crystal Caves - Tiny Hint'),
            Hint(['Caves Chunky'], '/supportedGames/dk64/images/chunky.png', 'Crystal Caves - Chunky Hint'),
            Hint(['Castle DK'], '/supportedGames/dk64/images/dk.png', 'Creepy Castle - DK Hint'),
            Hint(['Castle Diddy'], '/supportedGames/dk64/images/diddy.png', 'Creepy Castle - Diddy Hint'),
            Hint(['Castle Lanky'], '/supportedGames/dk64/images/lanky.png', 'Creepy Castle - Lanky Hint'),
            Hint(['Castle Tiny'], '/supportedGames/dk64/images/tiny.png', 'Creepy Castle - Tiny Hint'),
            Hint(['Castle Chunky'], '/supportedGames/dk64/images/chunky.png', 'Creepy Castle - Chunky Hint'),
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
            .replace("SNIDE", "Snide") \
            .replace("HAS GONE ON VACATION TO THE ", "can be found in") \
            .replace("GLORIOUS HILLS OF", "") \
            .replace("ARID SANDS OF", "") \
            .replace("OSHA VIOLATION HOTSPOT OF", "") \
            .replace("MURKY DEPTHS OF", "") \
            .replace("BLISSFUL GREENS OF", "") \
            .replace("MINERS PARADISE OF", "") \
            .replace("HAUNTED ARCHITECTURE OF", "") \
            .replace("TIMELESS CORRIDORS OF", "") \
            .replace("UNDENIABLE SERENITY OF", "") \
            .replace("ARCADE DWELLERS PARADISE OF", "") \
            .replace("RUBE GOLDBERG CACOPHONY OF", "") \
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
            ButtonLayout('Japes', 5),
            ButtonLayout('Aztec', 5),
            ButtonLayout('Factory', 5),
            ButtonLayout('Galleon', 5),
            ButtonLayout('Forest', 5),
            ButtonLayout('Caves', 5),
            ButtonLayout('Castle', 5),
            ButtonLayout('Instruments', 5),
            ButtonLayout('Shops', 4),
            ButtonLayout('Misc', 2)
        ]

    def isRowBasedLayout(self) -> bool:
        return False

    def getWidthGapBetweenButtons(self) -> int:
        return 10
