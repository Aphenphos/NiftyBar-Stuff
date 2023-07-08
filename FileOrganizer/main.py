import os
import shutil
import json
import sys
import atexit 
from datetime import datetime


ACTIONS_TAKEN = []


def init():
    #List SubDirectories in Specified Directory
    atexit.register(terminateProgram)
    if sys.argv[1] == "org":
        if sys.argv[2] != None:
            MAIN_DIR = sys.argv[2]
            listOfDirs = os.listdir(MAIN_DIR)
            for dir in listOfDirs:
        #Check SubDirectories for "Loose" files and organize them accordingly
                try:
                    processDir(f"{MAIN_DIR}{dir}")
                except:
                    terminateProgram()
        else:
            print("Please specify directory")
    elif sys.argv[1] == "undo":
        if sys.argv[2] == None :
            print("Please specify dumpfile location")
        else:
            undo(f"./dumps/{sys.argv[2]}.json")


def processDir(dirPath):
    directory = os.listdir(dirPath)
    files = [f for f in directory if os.path.isfile(dirPath+'/'+f)]
    if files != []:
        for file in files:
            print(f"File: {file} found in {dirPath}")
            fileDirName = file.split(".",1)[0]
            filePath = f"{dirPath}/{file}"
            newDirectory = f"{dirPath}/{fileDirName}"
            doesDirectoryExist = os.path.exists(newDirectory)


            if doesDirectoryExist == False:
                trackAction({"mkdir": newDirectory})
                os.mkdir(newDirectory)
                print(f"Directory: {newDirectory} created")
            
            trackAction({"mv": [filePath, newDirectory]})
            shutil.move(filePath, newDirectory)
            print(f"File: {filePath} moved to {newDirectory}")


def trackAction(action):
    ACTIONS_TAKEN.append(action)
    print("-")
    return

def terminateProgram():
    if ACTIONS_TAKEN != []:
        fileName = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

        with open(f"dumps/{fileName}.json", "w") as outfile:
            ACTIONStoJSON = json.dumps(ACTIONS_TAKEN)
            outfile.write(ACTIONStoJSON)

def undo(dumpFile):
    dumpData = parseDumpFile(dumpFile)
    processDumpData(dumpData)


def parseDumpFile(dumpFile):
    file = open(dumpFile)
    data = json.load(file)
    data.reverse()
    return data

def processDumpData(dumpData):
    #mvArr has the Old File location at 0 and the new directory at 1
    def mv(mvArr):
        fileName = mvArr[0].split("/")[-1]
        currentFileLocation = f"{mvArr[1]}/{fileName}"
        if os.path.isfile(currentFileLocation):
            shutil.move(f"{mvArr[1]}/{fileName}", mvArr[0])
        else:
            print(f"{currentFileLocation} not found")
            return
    def rmdir(dir):
        if os.path.isdir(dir):
            os.rmdir(dir)
        else:
            print(f"Directory {dir} not found")
            return
    actions = {
        "mv": mv,
        "mkdir": rmdir
    }

    for action in dumpData:
        keyValue = list(action.keys())[0]
        actions[keyValue](action[keyValue])

init()