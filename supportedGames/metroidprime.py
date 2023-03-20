from json import load

from game import Game
from hint import Hint

class MetroidPrime(Game):

    def __init__(self):
        super().__init__()

    def getGameNameText(self) -> str:
        return "Metroid Prime"

    def getHintList(self) -> list[Hint]:
        return [
            Hint('Artifact Locations')
        ]

    def readFromSpoilerLog(self, f) -> dict:
        with open(f) as myFile:
            data = load(myFile)
        locations = data['game_modifications'][0]['locations']
        locationsString = 'Artifact locations: '
        for x in locations:
            for y in locations.get(x):
                if 'Artifact' in locations.get(x).get(y):
                    locationsString += str(x) + " - " + str(y.split('/')[0]) + " (" + locations.get(x).get(y)[12:] + "), "
        result = {'Artifact Locations': locationsString[:-2]}
        print(locationsString[:-2])
        return result
