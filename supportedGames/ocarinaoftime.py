from json import load

from game import Game
from hint import Hint

class OcarinaOfTime(Game):

    def __init__(self):
        super().__init__()

    def getGameNameText(self) -> str:
        return "The Legend of Zelda: Ocarina of Time"

    def getHintList(self) -> list[Hint]:
        return [
            Hint('Colossus (Spirit Temple)'),
            Hint('DMC (Bombable Wall)'),
            Hint('DMC (Upper Grotto)'),
            Hint('DMT (Biggoron)'),
            Hint('DMT (Storms Grotto)'),
            Hint('Dodongos Cavern (Bombable Wall)'),
            Hint('GC (Maze)'),
            Hint('GC (Medigoron)'),
            Hint('GV (Waterfall)'),
            Hint('Graveyard (Shadow Temple)'),
            Hint('HC (Malon)'),
            Hint('HC (Rock Wall)'),
            Hint('HC (Storms Grotto)'),
            Hint('HF (Cow Grotto)'),
            Hint('HF (Near Market Grotto)'),
            Hint('HF (Open Grotto)'),
            Hint('HF (Southeast Grotto)'),
            Hint('KF (Deku Tree Left)'),
            Hint('KF (Deku Tree Right)'),
            Hint('KF (Outside Storms)'),
            Hint('KF (Storms Grotto)'),
            Hint('Kak (Open Grotto)'),
            Hint('LH (Lab)'),
            Hint('LH (Southeast Corner)'),
            Hint('LH (Southwest Corner)'),
            Hint('LW (Bridge)'),
            Hint('LW (Near Shortcuts Grotto)'),
            Hint('SFM (Maze Lower)'),
            Hint('SFM (Maze Upper)'),
            Hint('SFM (Saria)'),
            Hint('ToT (Left)'),
            Hint('ToT (Left-Center)'),
            Hint('ToT (Right)'),
            Hint('ToT (Right-Center)'),
            Hint('ZD (Mweep)'),
            Hint('ZF (Fairy)'),
            Hint('ZF (Jabu)'),
            Hint('ZR (Near Domain)'),
            Hint('ZR (Near Grottos)'),
            Hint('ZR (Open Grotto)')
        ]

    def readFromSpoilerLog(self, f) -> dict:
        with open(f) as myFile:
            data = load(myFile)
        gossipStoneJson = dict(data['gossip_stones'].items())
        result = {k: v['text'].replace('#', '') for k, v in gossipStoneJson.items()}
        return result
