from json import load

from buttonlayout import ButtonLayout
from game import Game
from hint import Hint

class OcarinaOfTime(Game):

    def __init__(self):
        super().__init__()

    def getGameNameText(self) -> str:
        return "The Legend of Zelda: Ocarina of Time"

    def getHintList(self) -> list[Hint]:
        return [
            Hint('Colossus (Spirit Temple)', '/supportedGames/ocarinaoftime/images/colossusspirittemple.png'),
            Hint('KF (Deku Tree Left)', '/supportedGames/ocarinaoftime/images/dekutreeleft.png'),
            Hint('KF (Deku Tree Right)', '/supportedGames/ocarinaoftime/images/dekutreeright.png'),
            Hint('DMC (Bombable Wall)', '/supportedGames/ocarinaoftime/images/dmcbombablewall.png'),
            Hint('DMC (Upper Grotto)', '/supportedGames/ocarinaoftime/images/dmcuppergrotto.png'),
            Hint('DMT (Biggoron)', '/supportedGames/ocarinaoftime/images/dmtbiggoron.png'),
            Hint('DMT (Storms Grotto)', '/supportedGames/ocarinaoftime/images/dmtstormsgrotto.png'),
            Hint('Dodongos Cavern (Bombable Wall)', '/supportedGames/ocarinaoftime/images/dcbombablewall.png'),
            Hint('GV (Waterfall)', '/supportedGames/ocarinaoftime/images/gvwaterfall.png'),
            Hint('GC (Maze)', '/supportedGames/ocarinaoftime/images/gcmaze.png'),
            Hint('GC (Medigoron)', '/supportedGames/ocarinaoftime/images/gcmedigoron.png'),
            Hint('HC (Malon)', '/supportedGames/ocarinaoftime/images/hcmalon.png'),
            Hint('HC (Rock Wall)', '/supportedGames/ocarinaoftime/images/hcrockwall.png'),
            Hint('HC (Storms Grotto)', '/supportedGames/ocarinaoftime/images/hcstormsgrotto.png'),
            Hint('HF (Cow Grotto)', '/supportedGames/ocarinaoftime/images/hfcowgrotto.png'),
            Hint('HF (Near Market Grotto)', '/supportedGames/ocarinaoftime/images/hfnearmarketgrotto.png'),
            Hint('HF (Open Grotto)', '/supportedGames/ocarinaoftime/images/hfopengrotto.png'),
            Hint('HF (Southeast Grotto)', '/supportedGames/ocarinaoftime/images/hfsoutheastgrotto.png'),
            Hint('Graveyard (Shadow Temple)', '/supportedGames/ocarinaoftime/images/graveyardshadowtemple.png'),
            Hint('Kak (Open Grotto)', '/supportedGames/ocarinaoftime/images/kakopengrotto.png'),
            Hint('KF (Outside Storms)', '/supportedGames/ocarinaoftime/images/kfoutsidestorms.png'),
            Hint('KF (Storms Grotto)', '/supportedGames/ocarinaoftime/images/kfstormsgrotto.png'),
            Hint('LH (Lab)', '/supportedGames/ocarinaoftime/images/lhlab.png'),
            Hint('LH (Southeast Corner)', '/supportedGames/ocarinaoftime/images/lhsoutheastcorner.png'),
            Hint('LH (Southwest Corner)', '/supportedGames/ocarinaoftime/images/lhsouthwestcorner.png'),
            Hint('LW (Bridge)', '/supportedGames/ocarinaoftime/images/lwbridge.png'),
            Hint('LW (Near Shortcuts Grotto)', '/supportedGames/ocarinaoftime/images/lwnearshortcutsgrotto.png'),
            Hint('SFM (Maze Lower)', '/supportedGames/ocarinaoftime/images/sfmmazelower.png'),
            Hint('SFM (Maze Upper)', '/supportedGames/ocarinaoftime/images/sfmmazeupper.png'),
            Hint('SFM (Saria)', '/supportedGames/ocarinaoftime/images/sfmsaria.png'),
            Hint('ToT (Left)', '/supportedGames/ocarinaoftime/images/totleft.png'),
            Hint('ToT (Left-Center)', '/supportedGames/ocarinaoftime/images/totcenterleft.png'),
            Hint('ToT (Right)', '/supportedGames/ocarinaoftime/images/totcenterright.png'),
            Hint('ToT (Right-Center)', '/supportedGames/ocarinaoftime/images/totright.png'),
            Hint('ZD (Mweep)', '/supportedGames/ocarinaoftime/images/zdmweep.png'),
            Hint('ZF (Fairy)', '/supportedGames/ocarinaoftime/images/zffairy.png'),
            Hint('ZF (Jabu)', '/supportedGames/ocarinaoftime/images/zfjabu.png'),
            Hint('ZR (Near Domain)', '/supportedGames/ocarinaoftime/images/zrneardomain.png'),
            Hint('ZR (Near Grottos)', '/supportedGames/ocarinaoftime/images/zrneargrottos.png'),
            Hint('ZR (Open Grotto)', '/supportedGames/ocarinaoftime/images/zropengrotto.png')
        ]

    def readFromSpoilerLog(self, f) -> dict:
        with open(f) as myFile:
            data = load(myFile)
        gossipStoneJson = dict(data['gossip_stones'].items())
        result = {k: v['text'].replace('#', '').replace('They say that ', '') for k, v in gossipStoneJson.items()}
        result = {k: v[0].upper() + v[1:] for k, v in result.items()}
        return result

    def getButtonLayout(self) -> list[ButtonLayout]:
        return [
            ButtonLayout('All', 40)
        ]

    def getWidthGapBetweenButtons(self) -> int:
        return 8

    def getHeightGapBetweenButtons(self) -> int:
        return 8

    def getMaxButtonsPerRow(self) -> int:
        return 8

    def getButtonWidth(self) -> int:
        return 100

    def getButtonHeight(self) -> int:
        return 100

    def isRowBasedLayout(self) -> bool:
        return True

    def isUsingSectionHeaders(self) -> bool:
        return False

    def isUsingTooltips(self) -> bool:
        return False