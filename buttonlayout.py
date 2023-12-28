class ButtonLayout:

    def __init__(self, label="", buttonCount=0):
        # The label which will appear above this row of buttons
        self.label = label

        # The number of buttons that will appear in this section
        self.buttonCount = buttonCount

    def setLabel(self, label):
        self.label = label

    def getLabel(self):
        return self.label

    def setButtonCount(self, buttonCount):
        self.buttonCount = buttonCount

    def getButtonCount(self):
        return self.buttonCount
