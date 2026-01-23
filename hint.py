class Hint:

    def __init__(self, keys=None, imagePath=None, buttonText="", sequenceNum=999, values=None, required=True):
        # A list of key(s) of this hint as they appear in the spoiler log
        # Having multiple keys in the list will mean multiple hints are associated with the same button
        # For example: in Donkey Kong 64 Randomizer hints are distributed in batches, rather than one at a time.
        if keys is None:
            keys = []
        self.keys = keys

        # The imagePath, if there is one, to be used on the button in the program for this hint
        self.imagePath = imagePath

        # The hint text as it appears in the spoiler log
        if values is None:
            values = [None for x in range(len(self.keys))]
        self.values = values

        # The text to be displayed on the button for this hint
        if buttonText == "":
            self.buttonText = ', '.join(keys)
        else:
            self.buttonText = buttonText

        # Used to determine the button order.
        # If all are set, 1 will appear first, 2 second, etc.
        # Default of 999 = no priority, will appear in order processed
        self.sequenceNum = sequenceNum

        # On by default. If set to false, the validator will bypass this hint when checking if every hint is populated
        self.required = required

    def setKeys(self, keys):
        self.keys = keys

    def getKeys(self):
        return self.keys

    def setImagePath(self, imagePath):
        self.imagePath = imagePath

    def getImagePath(self):
        return self.imagePath

    def setValues(self, values):
        self.values = values

    def getValues(self):
        return self.values

    def setValueAt(self, value, idx):
        self.values[idx] = value

    def getValueAt(self, idx):
        return self.values[idx]

    def setButtonText(self, buttonText):
        self.buttonText = buttonText

    def getButtonText(self):
        return self.buttonText

    def setSequenceNum(self, sequenceNum):
        self.sequenceNum = sequenceNum

    def getSequenceNum(self):
        return self.sequenceNum

    def getRequired(self):
        return self.required

    def setRequired(self, required):
        self.required = required
