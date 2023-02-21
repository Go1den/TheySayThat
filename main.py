import sys
from json import JSONDecodeError, dumps, load
from os import getcwd, path, access, W_OK
from shutil import copyfile

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QLabel, QMessageBox, QSystemTrayIcon

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.gossipStones = ['Colossus (Spirit Temple)',
                             'DMC (Bombable Wall)',
                             'DMC (Upper Grotto)',
                             'DMT (Biggoron)',
                             'DMT (Storms Grotto)',
                             'Dodongos Cavern (Bombable Wall)',
                             'GC (Maze)',
                             'GC (Medigoron)',
                             'GV (Waterfall)',
                             'Graveyard (Shadow Temple)',
                             'HC (Malon)',
                             'HC (Rock Wall)',
                             'HC (Storms Grotto)',
                             'HF (Cow Grotto)',
                             'HF (Near Market Grotto)',
                             'HF (Open Grotto)',
                             'HF (Southeast Grotto)',
                             'KF (Deku Tree Left)',
                             'KF (Deku Tree Right)',
                             'KF (Outside Storms)',
                             'KF (Storms Grotto)',
                             'Kak (Open Grotto)',
                             'LH (Lab)',
                             'LH (Southeast Corner)',
                             'LH (Southwest Corner)',
                             'LW (Bridge)',
                             'LW (Near Shortcuts Grotto)',
                             'SFM (Maze Lower)',
                             'SFM (Maze Upper)',
                             'SFM (Saria)',
                             'ToT (Left)',
                             'ToT (Left-Center)',
                             'ToT (Right)',
                             'ToT (Right-Center)',
                             'ZD (Mweep)',
                             'ZF (Fairy)',
                             'ZF (Jabu)',
                             'ZR (Near Domain)',
                             'ZR (Near Grottos)',
                             'ZR (Open Grotto)']

        trayIcon = QSystemTrayIcon(QIcon('TheySayThat.ico'), parent=self)
        trayIcon.setToolTip('TheySayThat')
        trayIcon.show()

        self.setFixedSize(880, 500)
        self.setWindowTitle("TheySayThat by Go1den")
        self.labelSpoilerLog = None
        self.labelOutputFile = None
        self.buttons = dict()
        self.hints = dict()
        self.spoilerLog = ""
        self.outputFile = (getcwd() + '/output.txt').replace('\\', '/')
        self.clickedButtons = []
        self.createButtons()
        self.loadConfig()
        self.createDefaultUI()
        self.show()
        isLogParsed = self.tryParseLog(self.spoilerLog)
        if not isLogParsed:
            self.setAllButtons(False)

    def closeEvent(self, event):
        resultDict = dict()
        if self.spoilerLog:
            resultDict['spoilerLog'] = self.spoilerLog
        if self.outputFile:
            resultDict['outputFile'] = self.outputFile
        if self.clickedButtons:
            resultDict['clickedButtons'] = self.clickedButtons
        self.clearFile('config.json')
        self.writeToFile('config.json', dumps(resultDict, indent=2))
        event.accept()

    def createDefaultUI(self):
        btn = QPushButton(self)
        btn.setText('Select Spoiler Log')
        btn.resize(200, 30)
        btn.move(10, 10)
        btn.clicked.connect(self.openSpoilerLog)
        btn.show()

        label = QLabel(self)
        label.setText("Current Spoiler Log: ")
        label.move(220, 10)
        label.show()

        self.labelSpoilerLog = QLabel(self)
        self.labelSpoilerLog.setText(self.spoilerLog)
        self.labelSpoilerLog.move(220, 25)
        self.labelSpoilerLog.show()

        btn2 = QPushButton(self)
        btn2.setText('Select Output File')
        btn2.resize(200, 30)
        btn2.move(10, 50)
        btn2.clicked.connect(self.openOutputFile)
        btn2.show()

        label2 = QLabel(self)
        label2.setText("Current Output File: ")
        label2.move(220, 50)
        label2.show()

        self.labelOutputFile = QLabel(self)
        self.labelOutputFile.setText(self.outputFile)
        self.labelOutputFile.move(220, 65)
        self.labelOutputFile.show()

        btn3 = QPushButton(self)
        btn3.setText('Reset Buttons and Clear Output File')
        btn3.resize(200, 30)
        btn3.move(670, 10)
        btn3.clicked.connect(lambda: self.clear(False))
        btn3.show()

    def isPathExistsOrCreateable(self, pathName):
        directoryName = path.dirname(pathName) or getcwd()
        try:
            return path.exists(pathName) or access(directoryName, W_OK)
        except OSError:
            return False

    def loadConfig(self):
        try:
            with open('config.json') as myFile:
                try:
                    data = load(myFile)
                    if data is not None:
                        try:
                            if data['spoilerLog'] != "" and self.isPathExistsOrCreateable(data['spoilerLog']):
                                self.spoilerLog = data['spoilerLog']
                        except KeyError:
                            pass
                        try:
                            if data['outputFile'] != "" and self.isPathExistsOrCreateable(data['outputFile']):
                                self.outputFile = data['outputFile']
                        except KeyError:
                            pass
                        try:
                            if data['clickedButtons'] is not None:
                                self.clickedButtons = data['clickedButtons']
                                self.disableClickedButtons()
                        except KeyError:
                            pass
                except JSONDecodeError:
                    return
        except FileNotFoundError:
            pass

    def disableClickedButtons(self):
        for button in self.clickedButtons:
            buttonText = button['buttonText']
            buttonToDisable = self.buttons[buttonText]
            if buttonToDisable is not None:
                buttonToDisable.setEnabled(False)

    def printHint(self, text, btn):
        try:
            resultString = self.hints.get(text)['text'].replace('#', '')
        except:
            return
        btn.setEnabled(False)
        self.clickedButtons.append({'buttonText': text})
        self.writeToFile(self.outputFile, resultString)

    def clear(self, override):
        reply = QMessageBox.No
        if not override:
            reply = QMessageBox.question(self, 'Confirm', 'Are you sure you want to reset all buttons and clear the output file?', QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.No)
        if override or reply == QMessageBox.Yes:
            isLogParsed = self.tryParseLog(self.spoilerLog)
            if not isLogParsed:
                self.setAllButtons(False)
            else:
                self.setAllButtons(True)
            self.clearFile(self.outputFile)
            self.clickedButtons = []

    def setAllButtons(self, setTo):
        for button in self.buttons:
            thisButton = self.buttons.get(button)
            thisButton.setEnabled(setTo)

    def clearFile(self, f):
        open(f, 'w').close()

    def writeToFile(self, f, text):
        with open(f, 'a') as myFile:
            myFile.write(text + '  ')

    def tryParseLog(self, log):
        if log is not None and log != "":
            try:
                with open(log) as myFile:
                    data = load(myFile)
                try:
                    hints = dict(data['gossip_stones'].items())
                    self.hints = hints
                    return True
                except KeyError:
                    self.showErrorMessage("Failed to import. Selected file is not a valid ZOOTR Spoiler Log.")
                    return False
            except FileNotFoundError:
                self.showErrorMessage("Failed to import. Selected file is not a valid ZOOTR Spoiler Log.")
                return False

    def openSpoilerLog(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Select Spoiler Log", "", "JSON File (*.json)", options=options)
        if not fileName:
            self.showErrorMessage("Invalid file path.")
            return
        fileName = fileName.replace('\\', '/')
        if not self.tryParseLog(fileName):
            return
        if fileName != self.spoilerLog:
            reply = QMessageBox.question(self, 'Confirm', 'Loading a new spoiler log will reset the buttons and clear the output file. Do you want to continue?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.spoilerLog = fileName
                self.labelSpoilerLog.setText(self.spoilerLog)
                self.labelSpoilerLog.adjustSize()
                self.clear(True)

    def showErrorMessage(self, msg):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText(msg)
        msgBox.setWindowTitle("Error")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()

    def openOutputFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Select Output File", "", "All Files (*);;Text Files (*.txt)", options=options)
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
        baseX = 10
        y = 100
        counter = 0
        for i in range(len(self.gossipStones)):
            hintKey = self.gossipStones[i]
            x = baseX + (counter % 4) * 220
            self.createButton(hintKey, x, y)
            if counter % 4 == 3:
                y = y + 40
            counter += 1

    def createButton(self, text, x, y):
        btn = QPushButton(self)
        btn.setText(text)
        btn.resize(200, 30)
        btn.move(x, y)
        btn.clicked.connect(lambda this, a=text, b=btn: self.printHint(a, b))
        btn.show()
        self.buttons[text] = btn

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('TheySayThat.ico'))
    win = MainWindow()
    sys.exit(app.exec_())
