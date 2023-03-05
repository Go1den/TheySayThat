from abc import ABC, abstractmethod
from copy import deepcopy

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
