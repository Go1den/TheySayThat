from json import load

from game import Game
from hint import Hint

class DonkeyKong64(Game):

    def __init__(self):
        super().__init__()

    def getGameNameText(self) -> str:
        return "Donkey Kong 64"

    def getHintList(self) -> list[Hint]:
        return [
            Hint('Progressive Slam'),
            Hint('Gorilla Gone'),
            Hint('Monkeyport'),
            Hint('Trombone'),
            Hint('Triangle'),
            Hint('Guitar'),
            Hint('Saxophone'),
            Hint('Bongos'),
            Hint('Aztec DK'),
            Hint('Aztec Diddy'),
            Hint('Aztec Lanky'),
            Hint('Aztec Tiny'),
            Hint('Aztec Chunky'),
            Hint('Castle DK'),
            Hint('Castle Diddy'),
            Hint('Castle Lanky'),
            Hint('Castle Tiny'),
            Hint('Castle Chunky'),
            Hint('Caves DK'),
            Hint('Caves Diddy'),
            Hint('Caves Lanky'),
            Hint('Caves Tiny'),
            Hint('Caves Chunky'),
            Hint('Factory DK'),
            Hint('Factory Diddy'),
            Hint('Factory Lanky'),
            Hint('Factory Tiny'),
            Hint('Factory Chunky'),
            Hint('Fungi DK'),
            Hint('Fungi Diddy'),
            Hint('Fungi Lanky'),
            Hint('Fungi Tiny'),
            Hint('Fungi Chunky'),
            Hint('Galleon DK'),
            Hint('Galleon Diddy'),
            Hint('Galleon Lanky'),
            Hint('Galleon Tiny'),
            Hint('Galleon Chunky'),
            Hint('Japes DK'),
            Hint('Japes Diddy'),
            Hint('Japes Lanky'),
            Hint('Japes Tiny'),
            Hint('Japes Chunky')
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
                        .replace("A KASPLAT", "a kasplat") \
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
