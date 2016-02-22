import os.path
import time
import datetime
import getpass
import glob
import os
import shutil


def main():
    startDownloads = '/Users/' + getpass.getuser() + '/Downloads/'
    startDesktop = '/Users/' + getpass.getuser() + '/Desktop/'
    endDir = '/Users/' + getpass.getuser() + '/Documents/Organized_Downloads/'
    if not os.path.exists(endDir):
        os.makedirs(endDir)
    for filename in os.listdir(startDownloads):
        if not filename.startswith('.'):
            modified = findModifiedTime(startDownloads + filename)
            if not os.path.exists(endDir + modified):
                os.makedirs(endDir + modified)
            shutil.move(
                startDownloads + filename, endDir + modified + '/' + filename)
    for filename in os.listdir(startDesktop):
        if not filename.startswith('.'):
            modified = findModifiedTime(startDesktop + filename)
            if not os.path.exists(endDir + modified):
                os.makedirs(endDir + modified)
            shutil.move(
                startDesktop + filename, endDir + modified + '/' + filename)

def findModifiedTime(filename):
    theTime = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(theTime).strftime('%Y-%m-%d')

if __name__ == '__main__':
    main()

# Make the plane transparent, and smaller in the robot class

