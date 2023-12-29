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
            Hint('Bongos', '/supportedGames/dk64/images/bongos.png', 'Bongos Hint'),
            Hint('Guitar', '/supportedGames/dk64/images/guitar.png', 'Guitar Hint'),
            Hint('Saxophone', '/supportedGames/dk64/images/saxophone.png', 'Saxophone Hint'),
            Hint('Trombone', '/supportedGames/dk64/images/trombone.png', 'Trombone Hint'),
            Hint('Triangle', '/supportedGames/dk64/images/triangle.png', 'Triangle Hint'),
            Hint('Aztec DK', '/supportedGames/dk64/images/dk.png', 'Angry Aztec - DK Hint'),
            Hint('Aztec Diddy', '/supportedGames/dk64/images/diddy.png', 'Angry Aztec - Diddy Hint'),
            Hint('Aztec Tiny', '/supportedGames/dk64/images/tiny.png', 'Angry Aztec - Tiny Hint'),
            Hint('Aztec Lanky', '/supportedGames/dk64/images/lanky.png', 'Angry Aztec - Lanky Hint'),
            Hint('Aztec Chunky', '/supportedGames/dk64/images/chunky.png', 'Angry Aztec - Chunky Hint'),
            Hint('Castle DK', '/supportedGames/dk64/images/dk.png', 'Creepy Castle - DK Hint'),
            Hint('Castle Diddy', '/supportedGames/dk64/images/diddy.png', 'Creepy Castle - Diddy Hint'),
            Hint('Castle Tiny', '/supportedGames/dk64/images/tiny.png', 'Creepy Castle - Tiny Hint'),
            Hint('Castle Lanky', '/supportedGames/dk64/images/lanky.png', 'Creepy Castle - Lanky Hint'),
            Hint('Castle Chunky', '/supportedGames/dk64/images/chunky.png', 'Creepy Castle - Chunky Hint'),
            Hint('Caves DK', '/supportedGames/dk64/images/dk.png', 'Crystal Caves - DK Hint'),
            Hint('Caves Diddy', '/supportedGames/dk64/images/diddy.png', 'Crystal Caves - Diddy Hint'),
            Hint('Caves Tiny', '/supportedGames/dk64/images/tiny.png', 'Crystal Caves - Tiny Hint'),
            Hint('Caves Lanky', '/supportedGames/dk64/images/lanky.png', 'Crystal Caves - Lanky Hint'),
            Hint('Caves Chunky', '/supportedGames/dk64/images/chunky.png', 'Crystal Caves - Chunky Hint'),
            Hint('Factory DK', '/supportedGames/dk64/images/dk.png', 'Frantic Factory - DK Hint'),
            Hint('Factory Diddy', '/supportedGames/dk64/images/diddy.png', 'Frantic Factory - Diddy Hint'),
            Hint('Factory Tiny', '/supportedGames/dk64/images/tiny.png', 'Frantic Factory - Tiny Hint'),
            Hint('Factory Lanky', '/supportedGames/dk64/images/lanky.png', 'Frantic Factory - Lanky Hint'),
            Hint('Factory Chunky', '/supportedGames/dk64/images/chunky.png', 'Frantic Factory - Chunky Hint'),
            Hint('Fungi DK', '/supportedGames/dk64/images/dk.png', 'Fungi Forest - DK Hint'),
            Hint('Fungi Diddy', '/supportedGames/dk64/images/diddy.png', 'Fungi Forest - Diddy Hint'),
            Hint('Fungi Tiny', '/supportedGames/dk64/images/tiny.png', 'Fungi Forest - Tiny Hint'),
            Hint('Fungi Lanky', '/supportedGames/dk64/images/lanky.png', 'Fungi Forest - Lanky Hint'),
            Hint('Fungi Chunky', '/supportedGames/dk64/images/chunky.png', 'Fungi Forest - Chunky Hint'),
            Hint('Galleon DK', '/supportedGames/dk64/images/dk.png', 'Gloomy Galleon - DK Hint'),
            Hint('Galleon Diddy', '/supportedGames/dk64/images/diddy.png', 'Gloomy Galleon - Diddy Hint'),
            Hint('Galleon Tiny', '/supportedGames/dk64/images/tiny.png', 'Gloomy Galleon - Tiny Hint'),
            Hint('Galleon Lanky', '/supportedGames/dk64/images/lanky.png', 'Gloomy Galleon - Lanky Hint'),
            Hint('Galleon Chunky', '/supportedGames/dk64/images/chunky.png', 'Gloomy Galleon - Chunky Hint'),
            Hint('Japes DK', '/supportedGames/dk64/images/dk.png', 'Jungle Japes - DK Hint'),
            Hint('Japes Diddy', '/supportedGames/dk64/images/diddy.png', 'Jungle Japes - Diddy Hint'),
            Hint('Japes Tiny', '/supportedGames/dk64/images/tiny.png', 'Jungle Japes - Tiny Hint'),
            Hint('Japes Lanky', '/supportedGames/dk64/images/lanky.png', 'Jungle Japes - Lanky Hint'),
            Hint('Japes Chunky', '/supportedGames/dk64/images/chunky.png', 'Jungle Japes - Chunky Hint'),
            Hint('Gorilla Gone', '/supportedGames/dk64/images/gorillagone.png', 'Gorilla Gone Hint'),
            Hint('Monkeyport', '/supportedGames/dk64/images/monkeyport.png', 'Monkeyport Hint'),
            Hint('Progressive Slam', '/supportedGames/dk64/images/progressiveslam.png', 'Progressive Slam Hint')
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
