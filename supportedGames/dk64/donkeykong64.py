from json import load

from buttonlayout import ButtonLayout
from game import Game
from hint import Hint

class DonkeyKong64(Game):

    def __init__(self):
        super().__init__()

    def getGameNameText(self) -> str:
        return "Donkey Kong 64"

    def getHintList(self) -> list[Hint]:
        return [
            Hint('Bongos', '/supportedGames/dk64/images/bongos.png'),
            Hint('Guitar', '/supportedGames/dk64/images/guitar.png'),
            Hint('Saxophone', '/supportedGames/dk64/images/saxophone.png'),
            Hint('Triangle', '/supportedGames/dk64/images/triangle.png'),
            Hint('Trombone', '/supportedGames/dk64/images/trombone.png'),
            Hint('Aztec DK', '/supportedGames/dk64/images/dk.png', 'DK'),
            Hint('Aztec Diddy', '/supportedGames/dk64/images/diddy.png', 'Diddy'),
            Hint('Aztec Tiny', '/supportedGames/dk64/images/tiny.png', 'Tiny'),
            Hint('Aztec Lanky', '/supportedGames/dk64/images/lanky.png', 'Lanky'),
            Hint('Aztec Chunky', '/supportedGames/dk64/images/chunky.png', 'Chunky'),
            Hint('Castle DK', '/supportedGames/dk64/images/dk.png', 'DK'),
            Hint('Castle Diddy', '/supportedGames/dk64/images/diddy.png', 'Diddy'),
            Hint('Castle Tiny', '/supportedGames/dk64/images/tiny.png', 'Tiny'),
            Hint('Castle Lanky', '/supportedGames/dk64/images/lanky.png', 'Lanky'),
            Hint('Castle Chunky', '/supportedGames/dk64/images/chunky.png', 'Chunky'),
            Hint('Caves DK', '/supportedGames/dk64/images/dk.png', 'DK'),
            Hint('Caves Diddy', '/supportedGames/dk64/images/diddy.png', 'Diddy'),
            Hint('Caves Tiny', '/supportedGames/dk64/images/tiny.png', 'Tiny'),
            Hint('Caves Lanky', '/supportedGames/dk64/images/lanky.png', 'Lanky'),
            Hint('Caves Chunky', '/supportedGames/dk64/images/chunky.png', 'Chunky'),
            Hint('Factory DK', '/supportedGames/dk64/images/dk.png', 'DK'),
            Hint('Factory Diddy', '/supportedGames/dk64/images/diddy.png', 'Diddy'),
            Hint('Factory Tiny', '/supportedGames/dk64/images/tiny.png', 'Tiny'),
            Hint('Factory Lanky', '/supportedGames/dk64/images/lanky.png', 'Lanky'),
            Hint('Factory Chunky', '/supportedGames/dk64/images/chunky.png', 'Chunky'),
            Hint('Fungi DK', '/supportedGames/dk64/images/dk.png', 'DK'),
            Hint('Fungi Diddy', '/supportedGames/dk64/images/diddy.png', 'Diddy'),
            Hint('Fungi Tiny', '/supportedGames/dk64/images/tiny.png', 'Tiny'),
            Hint('Fungi Lanky', '/supportedGames/dk64/images/lanky.png', 'Lanky'),
            Hint('Fungi Chunky', '/supportedGames/dk64/images/chunky.png', 'Chunky'),
            Hint('Galleon DK', '/supportedGames/dk64/images/dk.png', 'DK'),
            Hint('Galleon Diddy', '/supportedGames/dk64/images/diddy.png', 'Diddy'),
            Hint('Galleon Tiny', '/supportedGames/dk64/images/tiny.png', 'Tiny'),
            Hint('Galleon Lanky', '/supportedGames/dk64/images/lanky.png', 'Lanky'),
            Hint('Galleon Chunky', '/supportedGames/dk64/images/chunky.png', 'Chunky'),
            Hint('Japes DK', '/supportedGames/dk64/images/dk.png', 'DK'),
            Hint('Japes Diddy', '/supportedGames/dk64/images/diddy.png', 'Diddy'),
            Hint('Japes Tiny', '/supportedGames/dk64/images/tiny.png', 'Tiny'),
            Hint('Japes Lanky', '/supportedGames/dk64/images/lanky.png', 'Lanky'),
            Hint('Japes Chunky', '/supportedGames/dk64/images/chunky.png', 'Chunky'),
            Hint('Gorilla Gone', '/supportedGames/dk64/images/gorillagone.png'),
            Hint('Monkeyport', '/supportedGames/dk64/images/monkeyport.png'),
            Hint('Progressive Slam', '/supportedGames/dk64/images/progressiveslam.png')
        ]

    def readFromSpoilerLog(self, f) -> dict:
        with open(f, encoding='utf-8-sig') as myFile:
            data = load(myFile)
        allHints = dict()
        directItemHints = dict(data['Direct Item Hints'].items())
        wrinklyItemHints = dict(data['Wrinkly Hints'].items())
        for item in directItemHints.items():
            value = item[1].replace("YOU WOULD BE BETTER OFF LOOKING FOR SHOPS IN", "Look for shops in") \
                        .replace("YOU WOULD BE BETTER OFF LOOKING FOR", "Look for") \
                        .replace("YOU WOULD BE BETTER OFF LOOKING IN", "Look in") \
                        .replace("LADIES AND GENTLEMEN! IT APPEARS THAT ONE FIGHTER HAS COME UNEQUIPPED TO PROPERLY HANDLE THIS REPTILLIAN BEAST. PERHAPS THEY SHOULD HAVE LOOKED", "Look") \
                        .replace("FOR THE ELUSIVE SLAM.", "for the elusive Slam.") \
                        .replace("A FAIRY", "a fairy") \
                        .replace("A BATTLE CROWN", "a battle crown") \
                        .replace("A DIRT PATCH", "a dirt patch") \
                        .replace("A KASPLAT", "a Kasplat") \
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
                        .replace("FOR THIS.", "for this: " + item[0] + ".") \
                        .replace("OR", "or")
            value = value.replace("this: Monkeyport", "Monkeyport") \
                .replace("this: Guitar", "the Guitar") \
                .replace("this: Trombone", "the Trombone") \
                .replace("this: Triangle", "the Triangle") \
                .replace("this: Gorilla Gone", "Gorilla Gone") \
                .replace("this: Bongos", "the Bongos") \
                .replace("this: Saxophone", "the Saxophone")
            allHints[item[0]] = value
        for item in wrinklyItemHints.items():
            if item[0] == 'First Time Talk':
                continue
            allHints[item[0]] = item[1]
        result = {k: v for k, v in allHints.items()}
        return result

    def getMaxButtonsPerRow(self) -> int:
        return 5

    def getButtonWidth(self) -> int:
        return 64

    def getButtonHeight(self) -> int:
        return 64

    def getButtonLayout(self) -> list[ButtonLayout]:
        return [
            ButtonLayout('Instruments', 5),
            ButtonLayout('Aztec', 5),
            ButtonLayout('Castle', 5),
            ButtonLayout('Caves', 5),
            ButtonLayout('Factory', 5),
            ButtonLayout('Fungi', 5),
            ButtonLayout('Galleon', 5),
            ButtonLayout('Japes', 5),
            ButtonLayout('Other', 3)
        ]

    def isRowBasedLayout(self) -> bool:
        return False

    def getWidthGapBetweenButtons(self) -> int:
        return 10
