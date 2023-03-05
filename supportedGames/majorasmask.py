from game import Game
from hint import Hint

class MajorasMask(Game):

    def getGameNameText(self) -> str:
        return "The Legend of Zelda: Majora's Mask"

    def getHintList(self) -> list[Hint]:
        return [
            Hint('CanyonDock', 'Canyon Dock'),
            Hint('CanyonRavine', 'Canyon Ravine'),
            Hint('CanyonRoad', 'Canyon Road'),
            Hint('CanyonSpiritHouse', 'Canyon Spirit House'),
            Hint('MilkRoad', 'Milk Road'),
            Hint('MountainPath', 'Mountain Path'),
            Hint('MountainSpringFrog', 'Mountain Spring Frog'),
            Hint('MountainSpringPath', 'Mountain Spring Path'),
            Hint('OceanFortress', 'Ocean Fortress'),
            Hint('OceanZoraGame', 'Ocean Zora Game'),
            Hint('RanchBarn', 'Ranch Barn'),
            Hint('RanchCuccoShack', 'Ranch Cucco Shack'),
            Hint('RanchEntrance', 'Ranch Entrance'),
            Hint('RanchRacetrack', 'Ranch Racetrack'),
            Hint('RanchTree', 'Ranch Tree'),
            Hint('SwampPotionShop', 'Swamp Potion Shop'),
            Hint('SwampRoad', 'Swamp Road'),
            Hint('SwampSpiderHouse', 'Swamp Spider House'),
            Hint('TerminaEast', 'Termina East'),
            Hint('TerminaGossipDrums', 'Termina Gossip Drums'),
            Hint('TerminaGossipGuitar', 'Termina Gossip Guitar'),
            Hint('TerminaGossipLarge', 'Termina Gossip Large'),
            Hint('TerminaGossipPipes', 'Termina Gossip Pipes'),
            Hint('TerminaMilk', 'Termina Milk'),
            Hint('TerminaNorth', 'Termina North'),
            Hint('TerminaObservatory', 'Termina Observatory'),
            Hint('TerminaSouth', 'Termina South'),
            Hint('TerminaWest', 'Termina West')
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
                        value = text[1].strip().replace('.', '')
                        result[key] = value
                    if "TerminaWest" in line:
                        break
        return result
