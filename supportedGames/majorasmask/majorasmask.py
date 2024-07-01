from buttonlayout import ButtonLayout
from game import Game
from hint import Hint

class MajorasMask(Game):

    def getGameNameText(self) -> str:
        return "The Legend of Zelda: Majora's Mask"

    def getHintList(self) -> list[Hint]:
        return [
            Hint(['CanyonDock'], None, 'Canyon Dock'),
            Hint(['CanyonRavine'], None, 'Canyon Ravine'),
            Hint(['CanyonRoad'], None, 'Canyon Road'),
            Hint(['CanyonSpiritHouse'], None, 'Canyon Spirit House'),
            Hint(['MountainPath'], None, 'Mountain Path'),
            Hint(['MountainSpringFrog'], None, 'Mountain Spring Frog'),
            Hint(['MountainSpringPath'], None, 'Mountain Spring Path'),
            Hint(['OceanFortress'], None, 'Ocean Fortress'),
            Hint(['OceanZoraGame'], None, 'Ocean Zora Game'),
            Hint(['MilkRoad'], None, 'Milk Road'),
            Hint(['RanchBarn'], None, 'Ranch Barn'),
            Hint(['RanchCuccoShack'], None, 'Ranch Cucco Shack'),
            Hint(['RanchEntrance'], None, 'Ranch Entrance'),
            Hint(['RanchRacetrack'], None, 'Ranch Racetrack'),
            Hint(['RanchTree'], None, 'Ranch Tree'),
            Hint(['SwampPotionShop'], None, 'Swamp Potion Shop'),
            Hint(['SwampRoad'], None, 'Swamp Road'),
            Hint(['SwampSpiderHouse'], None, 'Swamp Spider House'),
            Hint(['TerminaGossipDrums'], None, 'Termina Gossip Drums'),
            Hint(['TerminaGossipGuitar'], None, 'Termina Gossip Guitar'),
            Hint(['TerminaGossipLarge'], None, 'Termina Gossip Large'),
            Hint(['TerminaGossipPipes'], None, 'Termina Gossip Pipes'),
            Hint(['TerminaNorth'], None, 'Termina North'),
            Hint(['TerminaEast'], None, 'Termina East'),
            Hint(['TerminaSouth'], None, 'Termina South'),
            Hint(['TerminaWest'], None, 'Termina West'),
            Hint(['TerminaMilk'], None, 'Termina Milk'),
            Hint(['TerminaObservatory'], None, 'Termina Observatory')
        ]

    def readFromSpoilerLog(self, f) -> dict:
        result = dict()
        with open(f) as myFile:
            foundGossipStones = False
            for line in myFile:
                if "Gossip Stone" in line and "Message" in line:
                    foundGossipStones = True
                if foundGossipStones:
                    if "->" in line and "MoonMask" not in line:
                        text = line.split('->')
                        key = text[0].strip()
                        value = text[1].strip().replace('...', '.')
                        result[key] = value
                    if "TerminaWest" in line:
                        break
        return result

    def getButtonLayout(self) -> list[ButtonLayout]:
        return [
            ButtonLayout('Canyon', 4),
            ButtonLayout('Mountain', 3),
            ButtonLayout('Ocean', 2),
            ButtonLayout('Ranch', 6),
            ButtonLayout('Swamp', 3),
            ButtonLayout('Termina', 10)
        ]
