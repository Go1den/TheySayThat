import sys
from json import JSONDecodeError, dumps, load
from os import getcwd
from shutil import copyfile

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QLabel, QMessageBox, QSystemTrayIcon, QComboBox, QFrame

from buttonlayout import ButtonLayout
from fileHelper import isPathExistsOrCreatable, writeToFile, fileContainsText, clearFile, readFileToString, writeToFileWithChosenIndent
from game import Game
from supportedGames.dk64.donkeykong64 import DonkeyKong64
from supportedGames.dk64.donkeykong64season4 import DonkeyKong64Season4
from supportedGames.dk64.donkeykong64batches import DonkeyKong64Batches
from supportedGames.dk64.donkeykong64batchesseason4 import DonkeyKong64BatchesSeason4
from supportedGames.majorasmask.majorasmask import MajorasMask
from supportedGames.metroidprime.metroidprime import MetroidPrime
from supportedGames.ocarinaoftime.ocarinaoftime import OcarinaOfTime

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.games: list[Game] = [
            DonkeyKong64Season4(),
            DonkeyKong64BatchesSeason4(),
            DonkeyKong64Batches(),
            DonkeyKong64(),
            OcarinaOfTime(),
            MajorasMask(),
            MetroidPrime()
        ]

        self.game: Game = OcarinaOfTime()

        trayIcon = QSystemTrayIcon(QIcon('TheySayThat.ico'), parent=self)
        trayIcon.setToolTip('TheySayThat')
        trayIcon.show()

        self.setFixedSize(880, 150)
        self.setWindowTitle("TheySayThat by Go1den")
        self.gameDropdown = None
        self.hintWritingModeDropdown = None
        self.resetButton = None
        self.labelSpoilerLog = None
        self.hintHandlerDropdown = None
        self.labelOutputFile = None
        self.buttons = dict()
        self.sectionLabels = dict()
        self.spoilerLog = ""
        self.outputFile = (getcwd() + '/output.txt').replace('\\', '/')
        self.hintHandler = "Filter duplicate hints"
        self.hintWritingMode = "Spaces"
        self.clickedButtons = []
        self.loadConfig()
        self.createDefaultUI()
        isLogParsed = self.tryParseLog(self.spoilerLog)
        self.createButtons()
        self.disableClickedButtons()
        self.show()

        if not isLogParsed:
            self.setAllButtons(False)
            self.showWarningMessage("The current spoiler log is not compatible with the chosen game. Please select a valid spoiler log.")

    def closeEvent(self, event):
        resultDict = dict()
        if self.game:
            resultDict['game'] = self.game.getGameName()
        if self.spoilerLog:
            resultDict['spoilerLog'] = self.spoilerLog
        if self.outputFile:
            resultDict['outputFile'] = self.outputFile
        if self.hintHandler:
            resultDict['hintHandler'] = self.hintHandler
        if self.hintWritingMode:
            resultDict['hintWritingMode'] = self.hintWritingMode
        if self.clickedButtons:
            resultDict['clickedButtons'] = self.clickedButtons
        clearFile('config.json')
        writeToFile('config.json', dumps(resultDict, indent=2))
        event.accept()

    def onGameChange(self, gameName):
        self.game = next((x for x in self.games if x.getGameName() == gameName), self.game)
        self.deleteAllButtonsAndSectionLabels()
        self.createButtons()
        if not self.game.isCurrentSpoilerLogValidForGame(self.spoilerLog):
            self.setAllButtons(False)
            self.clickedButtons = []
            self.showWarningMessage("The current spoiler log is not compatible with the chosen game. Please select a valid spoiler log.")
        else:
            if self.tryParseLog(self.spoilerLog):
                self.setAllButtons(True)
                self.promptClearOutputFile()
            else:
                self.showErrorMessage("The selected spoiler log is incompatible with the current game.")

    def onHintHandlerChange(self, hintHandler):
        self.hintHandler = hintHandler

    def onHintWritingModeChange(self, hintWritingMode):
        self.hintWritingMode = hintWritingMode

    def createDefaultUI(self):
        labelGameDropdown = QLabel(self)
        labelGameDropdown.setText("Game: ")
        labelGameDropdown.move(11, 11)
        labelGameDropdown.show()

        labelHintWritingMode = QLabel(self)
        labelHintWritingMode.setText("Separate hints in output file with: ")
        labelHintWritingMode.move(451, 11)
        labelHintWritingMode.show()

        labelHintHandler = QLabel(self)
        labelHintHandler.setText("Duplicate hint behavior: ")
        labelHintHandler.move(671, 11)
        labelHintHandler.show()

        hintWritingModes = ["One space", "Two spaces", "Four spaces", "Hyphens", "New lines"]
        try:
            indexToSet = hintWritingModes.index(self.hintWritingMode)
        except ValueError:
            indexToSet = 0
            self.hintHandler = "Filter duplicate hints"
        self.hintWritingModeDropdown = QComboBox(self)
        self.hintWritingModeDropdown.addItems(hintWritingModes)
        self.hintWritingModeDropdown.setCurrentIndex(indexToSet)
        self.hintWritingModeDropdown.currentTextChanged.connect(self.onHintWritingModeChange)
        self.hintWritingModeDropdown.resize(198, 28)
        self.hintWritingModeDropdown.move(451, 31)
        self.hintWritingModeDropdown.show()

        gameNames = [x.getGameName() for x in self.games]
        gameNames = sorted(gameNames)

        self.gameDropdown = QComboBox(self)
        self.gameDropdown.addItems(gameNames)
        self.gameDropdown.setCurrentIndex(gameNames.index(self.game.getGameName()))
        self.gameDropdown.currentTextChanged.connect(self.onGameChange)
        self.gameDropdown.resize(419, 28)
        self.gameDropdown.move(11, 31)
        self.gameDropdown.show()

        hintHandlers = ["Filter duplicate hints", "Count duplicate hints", "Always add every hint"]
        try:
            indexToSet = hintHandlers.index(self.hintHandler)
        except ValueError:
            indexToSet = 0
            self.hintHandler = "Filter duplicate hints"
        self.hintHandlerDropdown = QComboBox(self)
        self.hintHandlerDropdown.addItems(hintHandlers)
        self.hintHandlerDropdown.setCurrentIndex(indexToSet)
        self.hintHandlerDropdown.currentTextChanged.connect(self.onHintHandlerChange)
        self.hintHandlerDropdown.resize(198, 28)
        self.hintHandlerDropdown.move(671, 31)
        self.hintHandlerDropdown.show()

        btn = QPushButton(self)
        btn.setText('Select Spoiler Log')
        btn.resize(200, 30)
        btn.move(10, 70)
        btn.clicked.connect(self.openSpoilerLog)
        btn.show()

        label = QLabel(self)
        label.setText("Current Spoiler Log: ")
        label.move(220, 70)
        label.show()

        self.labelSpoilerLog = QLabel(self)
        self.labelSpoilerLog.setText(self.spoilerLog)
        self.labelSpoilerLog.move(220, 85)
        self.labelSpoilerLog.show()

        btn2 = QPushButton(self)
        btn2.setText('Select Output File')
        btn2.resize(200, 30)
        btn2.move(10, 110)
        btn2.clicked.connect(self.openOutputFile)
        btn2.show()

        label2 = QLabel(self)
        label2.setText("Current Output File: ")
        label2.move(220, 110)
        label2.show()

        self.labelOutputFile = QLabel(self)
        self.labelOutputFile.setText(self.outputFile)
        self.labelOutputFile.move(220, 125)
        self.labelOutputFile.show()

        self.resetButton = QPushButton(self)
        self.resetButton.setText('Reset Buttons')
        self.resetButton.resize(200, 30)
        self.resetButton.move(670, 70)
        self.resetButton.clicked.connect(lambda: self.resetButtons(False))
        self.resetButton.show()

        btn4 = QPushButton(self)
        btn4.setText('Clear Output File')
        btn4.resize(200, 30)
        btn4.move(670, 110)
        btn4.clicked.connect(lambda: self.clearOutputFile(False))
        btn4.show()

        hLine = QFrame(self)
        hLine.setFrameShape(QFrame.HLine)
        hLine.setFrameShadow(QFrame.Sunken)
        hLine.resize(860, 4)
        hLine.move(10, 150)
        hLine.show()

    def loadConfig(self):
        try:
            with open('config.json') as myFile:
                try:
                    data = load(myFile)
                    if data is not None:
                        try:
                            if data['spoilerLog'] != "" and isPathExistsOrCreatable(data['spoilerLog']):
                                self.spoilerLog = data['spoilerLog']
                        except KeyError:
                            pass
                        try:
                            if data['outputFile'] != "" and isPathExistsOrCreatable(data['outputFile']):
                                self.outputFile = data['outputFile']
                        except KeyError:
                            pass
                        try:
                            if data['clickedButtons'] is not None:
                                self.clickedButtons = data['clickedButtons']
                        except KeyError:
                            pass
                        try:
                            if data['game'] is not None:
                                self.game = next((x for x in self.games if x.getGameName() == data['game']), self.game)
                        except KeyError:
                            self.game = self.game
                        try:
                            if data['hintHandler'] is not None:
                                self.hintHandler = data['hintHandler']
                        except KeyError:
                            pass
                        try:
                            if data['hintWritingMode'] is not None:
                                self.hintWritingMode = data['hintWritingMode']
                        except KeyError:
                            pass
                except JSONDecodeError:
                    return
        except FileNotFoundError:
            pass

    def disableClickedButtons(self):
        for buttonKey in self.clickedButtons:
            try:
                buttonToDisable = self.buttons[buttonKey]
            except KeyError:
                continue
            if buttonToDisable is not None:
                buttonToDisable.setEnabled(False)

    def getIndent(self):
        if self.hintWritingMode == "One space":
            return " "
        if self.hintWritingMode == "Four spaces":
            return "    "
        if self.hintWritingMode == "Hyphens":
            return " - "
        if self.hintWritingMode == "New lines":
            return "\n"
        return "  "  # Default is Two spaces

    def printHint(self, btn, buttonKey):
        indent = self.getIndent()
        btn.setEnabled(False)
        self.clickedButtons.append(buttonKey)
        hintTextList = self.game.getHints()[buttonKey].getValues()
        for hintText in hintTextList:
            if self.hintHandler == "Always add every hint":
                writeToFileWithChosenIndent(self.outputFile, hintText, indent)
                continue
            hintAlreadyExists = fileContainsText(self.outputFile, hintText)
            if not hintAlreadyExists:
                writeToFileWithChosenIndent(self.outputFile, hintText, indent)
                continue
            if self.hintHandler == "Count duplicate hints":
                fileContents = readFileToString(self.outputFile)
                idx = fileContents.index(hintText)
                if idx >= 0:
                    checkIndex = idx + len(hintText)
                    potentialCountString = fileContents[checkIndex:checkIndex + 5]
                    if ' (x' in potentialCountString and ')' in potentialCountString:
                        currentCount = int(fileContents[checkIndex + 3])
                        result = fileContents[:checkIndex + 3] + str(currentCount + 1) + fileContents[checkIndex + 4:]
                    else:
                        result = fileContents[:checkIndex] + ' (x2)' + fileContents[checkIndex:]
                    clearFile(self.outputFile)
                    writeToFileWithChosenIndent(self.outputFile, result, None)
                else:  # Should not be possible
                    writeToFileWithChosenIndent(self.outputFile, hintText, indent)

    def resetButtons(self, override):
        reply = QMessageBox.No
        if not override:
            reply = QMessageBox.question(self, 'Confirm', 'Are you sure you want to reset all buttons?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if override or reply == QMessageBox.Yes:
            self.setAllButtons(True)
            self.clickedButtons = []

    def promptClearOutputFile(self):
        reply = QMessageBox.question(self, 'Confirm', 'The current spoiler log is still compatible with the chosen game. Would you like to clear the output file?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            clearFile(self.outputFile)

    def clearOutputFile(self, override):
        reply = QMessageBox.No
        if not override:
            reply = QMessageBox.question(self, 'Confirm', 'Are you sure you want to clear the output file?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if override or reply == QMessageBox.Yes:
            clearFile(self.outputFile)

    def setAllButtons(self, setTo):
        for button in self.buttons:
            thisButton = self.buttons.get(button)
            thisButton.setEnabled(setTo)
        self.resetButton.setEnabled(setTo)

    def tryParseLog(self, log):
        try:
            if log is not None and log != "" and self.game is not None:
                result = self.game.update(log)
                if not result or not self.game.allKeysHaveHints():
                    raise Exception
                return True
        except:
            return False

    def openSpoilerLog(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Select Spoiler Log", "", "All Files (*.*)", options=options)
        if not fileName:
            self.showErrorMessage("Invalid file path.")
            return
        fileName = fileName.replace('\\', '/')
        if not self.tryParseLog(fileName):
            self.showErrorMessage("The selected spoiler log is incompatible with the current game.")
            return
        if fileName != self.spoilerLog:
            reply = QMessageBox.question(self, 'Confirm', 'Loading a new spoiler log will reset the buttons and clear the output file. Do you want to continue?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.spoilerLog = fileName
                self.labelSpoilerLog.setText(self.spoilerLog)
                self.labelSpoilerLog.adjustSize()
                self.clearOutputFile(True)
                self.resetButtons(True)

    def showWarningMessage(self, msg):
        msgBox = QMessageBox(self)
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText(msg)
        msgBox.setWindowTitle("Warning")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()

    def showErrorMessage(self, msg):
        msgBox = QMessageBox(self)
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText(msg)
        msgBox.setWindowTitle("Error")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()

    def openOutputFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Select Output File", "", "All Files (*.*)", options=options)
        if not fileName:
            self.showErrorMessage("Invalid file path.")
            return
        fileName = fileName.replace('\\', '/')
        if self.outputFile != fileName:
            reply = QMessageBox.question(self, 'Confirm', 'Would you like to copy the contents of the previous output file to this one?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                try:
                    copyfile(self.outputFile, fileName)
                except:
                    self.showErrorMessage("Attempt to copy from the previous file was unsuccessful.")
            self.outputFile = fileName
            self.labelOutputFile.setText(self.outputFile)
            self.labelOutputFile.adjustSize()

    def createButtons(self):
        if self.game is None:
            return
        if not self.game.getButtonLayout():
            self.createLegacyLayout()
        elif self.game.isRowBasedLayout():
            self.createRowBasedLayout()
        else:
            self.createColumnBasedLayout()

    def createColumnBasedLayout(self):
        x = 10
        nextX = 10
        baseY = 160
        counter = 0
        maxEntriesInColumn = 0
        buttonLayout = self.game.getButtonLayout()
        currentSection = ButtonLayout("None", 0)
        hints = self.game.getHints()
        for i in range(len(hints)):
            if currentSection.getButtonCount() == 0:
                x = nextX
                currentSection = buttonLayout.pop(0)
                if currentSection.getButtonCount() > maxEntriesInColumn:
                    maxEntriesInColumn = min(currentSection.getButtonCount(), self.game.getMaxButtonsPerColumn())
                self.createSectionLabel(currentSection.getLabel(), x, baseY)
                nextX = x + self.game.getButtonWidth() + self.game.getWidthGapBetweenButtons()
                y = baseY + 20
                counter = 0
            buttonText = hints[i].getButtonText()
            y = baseY + 20 + (counter % self.game.getMaxButtonsPerColumn()) * (self.game.getButtonHeight() + self.game.getHeightGapBetweenButtons())
            self.createButton(buttonText, x, y, hints[i].getImagePath())
            currentSection.setButtonCount(currentSection.getButtonCount() - 1)
            if counter % self.game.getMaxButtonsPerColumn() == self.game.getMaxButtonsPerColumn() - 1:
                nextX = x + self.game.getButtonWidth() + self.game.getWidthGapBetweenButtons()
                x = x + self.game.getButtonWidth() + self.game.getWidthGapBetweenButtons()
            counter += 1
        if counter % self.game.getMaxButtonsPerColumn() != 0:  # the bottom most row of buttons won't show if it contains fewer than max amount of buttons per row unless we do this
            x = x + self.game.getButtonWidth() + self.game.getWidthGapBetweenButtons()
        self.setFixedSize(880, baseY + 20 + maxEntriesInColumn * (self.game.getButtonHeight() + self.game.getHeightGapBetweenButtons()))

    def createRowBasedLayout(self):
        baseX = 10
        y = 160
        counter = 0
        buttonLayout = self.game.getButtonLayout()
        currentSection = ButtonLayout("None", 0)
        hints = self.game.getHints()
        for i in range(len(hints)):
            if currentSection.getButtonCount() == 0 and self.game.isUsingSectionHeaders():
                if counter % self.game.getMaxButtonsPerRow() != 0:
                    y = y + self.game.getButtonHeight() + self.game.getHeightGapBetweenButtons()
                currentSection = buttonLayout.pop(0)
                self.createSectionLabel(currentSection.getLabel(), baseX, y)
                y = y + 20
                counter = 0
            buttonText = hints[i].getButtonText()
            x = baseX + (counter % self.game.getMaxButtonsPerRow()) * (self.game.getButtonWidth() + self.game.getWidthGapBetweenButtons())
            self.createButton(buttonText, x, y, hints[i].getImagePath())
            currentSection.setButtonCount(currentSection.getButtonCount() - 1)
            if counter % self.game.getMaxButtonsPerRow() == self.game.getMaxButtonsPerRow() - 1:
                y = y + self.game.getButtonHeight() + self.game.getHeightGapBetweenButtons()
            counter += 1
        if counter % self.game.getMaxButtonsPerRow() != 0:  # the bottom most row of buttons won't show if it contains fewer than max amount of buttons per row unless we do this
            y = y + self.game.getButtonHeight() + 10 # Make the bottom line up with the 10 pixel gap on the left and top
        self.setFixedSize(880, y)

    def createLegacyLayout(self):
        baseX = 10
        y = 160
        counter = 0
        hints = self.game.getHints()
        for i in range(len(hints)):
            buttonText = hints[i].getButtonText()
            x = baseX + (counter % 4) * 220
            self.createButton(buttonText, x, y)
            if counter % 4 == 3:
                y = y + 40
            counter += 1
        if counter % 4 != 0:  # the bottom most row of buttons won't show if it contains fewer than 4 buttons unless we do this
            y = y + 40
        self.setFixedSize(880, y)

    def createSectionLabel(self, text, x, y):
        labelSection = QLabel(self)
        labelSection.setText(text)
        labelSection.move(x, y)
        labelSection.show()
        self.sectionLabels[text] = labelSection

    def createButton(self, buttonText, x, y, imagePath=None):
        btn = QPushButton(self)
        btn.resize(self.game.getButtonWidth(), self.game.getButtonHeight())
        if imagePath:
            btn.setIcon(QIcon(getcwd() + imagePath))
            btn.setIconSize(QSize(self.game.getButtonWidth(), self.game.getButtonHeight()))
            if self.game.isUsingTooltips():
                btn.setToolTip(buttonText)
        else:
            btn.setText(buttonText)
        btn.move(x, y)
        buttonKey = len(self.buttons)
        btn.clicked.connect(lambda this, a=btn, b=buttonKey: self.printHint(a, b))
        btn.show()
        self.buttons[buttonKey] = btn

    def deleteAllButtonsAndSectionLabels(self):
        for button in self.buttons:
            self.buttons.get(button).hide()
            self.buttons.get(button).deleteLater()
        for label in self.sectionLabels:
            self.sectionLabels.get(label).hide()
            self.sectionLabels.get(label).deleteLater()
        self.buttons = dict()
        self.sectionLabels = dict()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('TheySayThat.ico'))
    win = MainWindow()
    sys.exit(app.exec_())
