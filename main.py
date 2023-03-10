import sys
from json import JSONDecodeError, dumps, load
from os import getcwd
from shutil import copyfile

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QLabel, QMessageBox, QSystemTrayIcon, QComboBox, QFrame

from fileHelper import isPathExistsOrCreatable, writeToFile, fileContainsText, clearFile, readFileToString
from game import Game
from supportedGames.donkeykong64 import DonkeyKong64
from supportedGames.majorasmask import MajorasMask
from supportedGames.ocarinaoftime import OcarinaOfTime

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.games: list[Game] = [
            DonkeyKong64(),
            OcarinaOfTime(),
            MajorasMask()
        ]

        self.game: Game = OcarinaOfTime()

        trayIcon = QSystemTrayIcon(QIcon('TheySayThat.ico'), parent=self)
        trayIcon.setToolTip('TheySayThat')
        trayIcon.show()

        self.setFixedSize(880, 150)
        self.setWindowTitle("TheySayThat by Go1den")
        self.gameDropdown = None
        self.resetButton = None
        self.labelSpoilerLog = None
        self.hintHandlerDropdown = None
        self.labelOutputFile = None
        self.buttons = dict()
        self.spoilerLog = ""
        self.outputFile = (getcwd() + '/output.txt').replace('\\', '/')
        self.hintHandler = "Filter them"
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
        if self.clickedButtons:
            resultDict['clickedButtons'] = self.clickedButtons
        clearFile('config.json')
        writeToFile('config.json', dumps(resultDict, indent=2))
        event.accept()

    def onGameChange(self, gameName):
        self.game = next((x for x in self.games if x.getGameName() == gameName), self.game)
        self.deleteAllButtons()
        self.createButtons()
        if not self.game.isCurrentSpoilerLogValidForGame(self.spoilerLog):
            self.setAllButtons(False)
            self.clickedButtons = []
            self.showWarningMessage("The current spoiler log is not compatible with the chosen game. Please select a valid spoiler log.")
        else:
            self.setAllButtons(True)

    def onHintHandlerChange(self, hintHandler):
        self.hintHandler = hintHandler

    def createDefaultUI(self):
        gameNames = [x.getGameName() for x in self.games]
        gameNames = sorted(gameNames)

        self.gameDropdown = QComboBox(self)
        self.gameDropdown.addItems(gameNames)
        self.gameDropdown.setCurrentIndex(gameNames.index(self.game.getGameName()))
        self.gameDropdown.currentTextChanged.connect(self.onGameChange)
        self.gameDropdown.resize(419, 28)
        self.gameDropdown.move(11, 11)
        self.gameDropdown.show()

        labelHintHandler = QLabel(self)
        labelHintHandler.setText("Duplicate Hint Behavior: ")
        labelHintHandler.move(550, 19)
        labelHintHandler.show()

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
        self.hintHandlerDropdown.move(671, 11)
        self.hintHandlerDropdown.show()

        btn = QPushButton(self)
        btn.setText('Select Spoiler Log')
        btn.resize(200, 30)
        btn.move(10, 50)
        btn.clicked.connect(self.openSpoilerLog)
        btn.show()

        label = QLabel(self)
        label.setText("Current Spoiler Log: ")
        label.move(220, 50)
        label.show()

        self.labelSpoilerLog = QLabel(self)
        self.labelSpoilerLog.setText(self.spoilerLog)
        self.labelSpoilerLog.move(220, 65)
        self.labelSpoilerLog.show()

        btn2 = QPushButton(self)
        btn2.setText('Select Output File')
        btn2.resize(200, 30)
        btn2.move(10, 90)
        btn2.clicked.connect(self.openOutputFile)
        btn2.show()

        label2 = QLabel(self)
        label2.setText("Current Output File: ")
        label2.move(220, 90)
        label2.show()

        self.labelOutputFile = QLabel(self)
        self.labelOutputFile.setText(self.outputFile)
        self.labelOutputFile.move(220, 105)
        self.labelOutputFile.show()

        self.resetButton = QPushButton(self)
        self.resetButton.setText('Reset Buttons')
        self.resetButton.resize(200, 30)
        self.resetButton.move(670, 50)
        self.resetButton.clicked.connect(lambda: self.resetButtons(False))
        self.resetButton.show()

        btn4 = QPushButton(self)
        btn4.setText('Clear Output File')
        btn4.resize(200, 30)
        btn4.move(670, 90)
        btn4.clicked.connect(lambda: self.clearOutputFile(False))
        btn4.show()

        hLine = QFrame(self)
        hLine.setFrameShape(QFrame.HLine)
        hLine.setFrameShadow(QFrame.Sunken)
        hLine.resize(860, 4)
        hLine.move(10, 130)
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
                except JSONDecodeError:
                    return
        except FileNotFoundError:
            pass

    def disableClickedButtons(self):
        for button in self.clickedButtons:
            buttonText = button['buttonText']
            try:
                buttonToDisable = self.buttons[buttonText]
            except KeyError:
                continue
            if buttonToDisable is not None:
                buttonToDisable.setEnabled(False)

    def printHint(self, buttonText, btn):
        btn.setEnabled(False)
        self.clickedButtons.append({'buttonText': buttonText})
        hintText = next((x.value for x in self.game.getHints() if x.buttonText == buttonText), "")
        if self.hintHandler == "Always add every hint":
            writeToFile(self.outputFile, hintText)
            return
        hintAlreadyExists = fileContainsText(self.outputFile, hintText)
        if not hintAlreadyExists:
            writeToFile(self.outputFile, hintText)
            return
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
                writeToFile(self.outputFile, result.rstrip())
            else:  # Should not be possible
                writeToFile(self.outputFile, hintText)

    def resetButtons(self, override):
        reply = QMessageBox.No
        if not override:
            reply = QMessageBox.question(self, 'Confirm', 'Are you sure you want to reset all buttons?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if override or reply == QMessageBox.Yes:
            self.setAllButtons(True)
            self.clickedButtons = []

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
        baseX = 10
        y = 140
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

    def createButton(self, buttonText, x, y):
        btn = QPushButton(self)
        btn.setText(buttonText)
        btn.resize(200, 30)
        btn.move(x, y)
        btn.clicked.connect(lambda this, a=buttonText, b=btn: self.printHint(a, b))
        btn.show()
        self.buttons[buttonText] = btn

    def deleteAllButtons(self):
        for button in self.buttons:
            self.buttons.get(button).deleteLater()
        self.buttons = dict()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('TheySayThat.ico'))
    win = MainWindow()
    sys.exit(app.exec_())
