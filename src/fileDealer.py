import os
import shutil

# Path of the directory that will receive the the files that will be distributed
incoming = r''
# Path of the file that will hold the history(.txt) 
history = r''
# Paths of the directories that will receive the copies
# each path must be assigned to one variable and included into the directories list(directories)
dir1 = r''
dir2 = r''
dir3 = r''
# List containing all the directories that will receive the files
directories = [dir1, dir2, dir3]
def getFileNames(dirPath):
  for root, dirs, fileNames in os.walk(dirPath):
    files = fileNames
  return files

def readHistory(historyFile):
  with open(historyFile, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    files = []
    for line in lines:
      files.append(line.replace('\n',''))
  return files

def saveFilesToHistory(filesArray, historyFile):
  historyFiles = readHistory(historyFile)
  for file in filesArray:
    if file not in historyFiles:
      with open(historyFile, 'a', encoding='utf-8') as f:
        f.write(f'{file}\n')

def saveFileToDir(originPath, targetPath, fileName):
  shutil.copyfile(f'{originPath}/{fileName}', f'{targetPath}/{fileName}')

def deliverFiles(originPath, targetsPathsArray, historyFile):
  fileNames = getFileNames(originPath)
  historyFiles = readHistory(historyFile)
  for file in fileNames:
    if file not in historyFiles:
      for target in targetsPathsArray:
        saveFileToDir(originPath, target, file)
  saveFilesToHistory(fileNames, historyFile)

deliverFiles(incoming, directories, history)

