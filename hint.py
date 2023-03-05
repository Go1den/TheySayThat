class Hint:

    def __init__(self, key="", buttonText="", sequenceNum=999, value=""):
        # The key of this hint as it appears in the spoiler log
        self.key = key

        # The hint text as it appears in the spoiler log
        self.value = value

        # The text to be displayed on the button for this hint
        if buttonText == "":
            self.buttonText = key
        else:
            self.buttonText = buttonText

        # Used to determine the button order.
        # If all are set, 1 will appear first, 2 second, etc.
        # Default of 999 = no priority, will appear in order processed
        self.sequenceNum = sequenceNum

    def setKey(self, key):
        self.key = key

    def getKey(self):
        return self.key

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def setButtonText(self, buttonText):
        self.buttonText = buttonText

    def getButtonText(self):
        return self.buttonText

    def setSequenceNum(self, sequenceNum):
        self.sequenceNum = sequenceNum

    def getSequenceNum(self):
        return self.sequenceNum
