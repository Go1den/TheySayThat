from abc import ABC, abstractmethod
from copy import deepcopy

from buttonlayout import ButtonLayout
from hint import Hint

class Game(ABC):

    def __init__(self):
        self.hints = self.getHintList()
        self.hintDict = dict()
        self.gameName = self.getGameNameText()

    @abstractmethod  # Must be implemented in a new game class
    def getGameNameText(self) -> str:
        """
        Returns:
            str: Name of the video game.
        """
        return "Game Name Not Found"

    # Override in child class if you wish to modify the default
    def isRowBasedLayout(self) -> bool:
        """
        Returns:
            bool: Boolean indicating whether the buttons should be added to the layout in rows (True) or columns (False). Default is True for row based layout.
        """
        return True

    # Override in child class if you wish to modify the default
    def getMaxButtonsPerRow(self) -> int:
        """
        Returns:
            int: The maximum number of buttons allowed in any row of the layout. The default layout only permits 4 buttons in a row, but this can be overridden here.
        """
        return 4

    # Override in child class if you wish to modify the default
    def getButtonHeight(self) -> int:
        """
        Returns:
            int: The height (in pixels) of each button in the layout. By default, this is 30 pixels.
        """
        return 30

    # Override in child class if you wish to modify the default
    def getButtonWidth(self) -> int:
        """
        Returns:
            int: The width (in pixels) of each button in the layout. By default, this is 200 pixels.
        """
        return 200

    # Override in child class if you wish to modify the default
    def getWidthGapBetweenButtons(self) -> int:
        """
        Returns:
            int: The width (in pixels) of the gap between each button in a row. By default, this is 20 pixels.
        """
        return 20

    # Override in child class if you wish to modify the default
    def getHeightGapBetweenButtons(self) -> int:
        """
        Returns:
            int: The height (in pixels) of the gap between each button in a column. By default, this is 10 pixels.
        """
        return 10

    # Override in child class if you wish to modify the default
    def getButtonLayout(self) -> list[ButtonLayout]:
        """
        Returns:
            list[ButtonLayout]: A list of button layout objects indicating how many buttons you want in each section of the layout.
            Each ButtonLayout object specifies a label for that section of the layout, as well as how many buttons will appear in that section.
        """
        return []

    @abstractmethod  # Must be implemented in a new game class
    def getHintList(self) -> list[Hint]:
        """
        Returns:
            list[Hint]: A list of hint objects representing each hint location in the game.
        """
        return []

    @abstractmethod  # Must be implemented in a new game class
    def readFromSpoilerLog(self, f) -> dict:
        """Parses the given file and returns a dictionary containing hint text.

        Do not call this method directly. When you want to update the hint list,
        call setHintList instead, which encapsulates this method.

        Args:
            f (str): The path to some spoiler log file

        Returns:
            dict: Keys are the hint locations, values are the text of those hints.
        """
        return dict()

    # THE METHODS BELOW THIS POINT ARE UNIVERSAL AND DO NOT NEED TO BE IMPLEMENTED FOR NEW GAMES.

    def update(self, f) -> bool:
        """Reads from the given spoiler log and updates the game information.

        Args:
            f (str): The path to some spoiler log file

        Returns:
            bool: True if both setting the hint dictionary and setting the hints
            were successful. False if either step failed.
        """
        return self.setHintDict(f) and self.setHintText()

    def setHintDict(self, f) -> bool:
        """Parses the given file and returns a dictionary containing hint text.

        The hintDict is only updated if the readFromSpoilerLog returns properly.
        On an error, it reverts to its previous value.

        Args:
            f (str): The path to some spoiler log file

        Returns:
            bool: Indicates success or failure of reading from the spoiler log
            and updating self.hintList
        """
        temp = deepcopy(self.hintDict)
        try:
            self.hintDict = self.readFromSpoilerLog(f)
            return True
        except:
            self.hintDict = temp
            return False

    def setHintText(self) -> bool:
        """Creates the list of hint objects using all the collected information.

        The hint list is only updated if there are no exceptions during execution.
        If an exception occurs, the list will revert.

        Returns:
            bool: Indicates success or failure of creating the hint object list.
        """
        temp = deepcopy(self.hints)
        try:
            hintKeyList = [x.key for x in self.hints]
            for entry in self.hintDict:
                idx = hintKeyList.index(entry)
                if idx is not None:
                    self.hints[idx].setValue(self.hintDict.get(entry))
            self.hints.sort(key=lambda x: x.sequenceNum)
            return True
        except:
            self.hints = temp
            return False

    def getHints(self) -> list[Hint]:
        return self.hints

    def getGameName(self) -> str:
        return self.gameName

    def allKeysHaveHints(self) -> bool:
        for hint in self.hints:
            if hint.value is None or hint.value == "":
                return False
        return True

    def isCurrentSpoilerLogValidForGame(self, log):
        try:
            parsedHints = len(self.readFromSpoilerLog(log))
            return parsedHints == len(self.getHintList())
        except:
            return False
