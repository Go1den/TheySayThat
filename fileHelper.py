from os import path, getcwd, access, W_OK

def isPathExistsOrCreatable(pathName):
    directoryName = path.dirname(pathName) or getcwd()
    try:
        return path.exists(pathName) or access(directoryName, W_OK)
    except OSError:
        return False

def writeToFile(f, text):
    with open(f, 'a') as myFile:
        myFile.write(text + '  ')

def writeToFileWithChosenIndent(f, text, indent):
    with open(f, 'a') as myFile:
        myFile.write(text + indent)

def fileContainsText(file, text) -> bool:
    with open(file) as f:
        if text in f.read():
            return True
    return False

def clearFile(f):
    open(f, 'w').close()

def readFileToString(f) -> str:
    with open(f, 'r') as myFile:
        result = myFile.read()
    return result
