#!/usr/bin/python3

from os import walk
from os import path

from models.track import Track

def getAllTracks(myPath):
    i = 0
    track_objects = []
    tracks = getFiles(myPath)
    for a in tracks:
        track_objects.append(Track(a,i))
        i = i+1
    for tr in track_objects:
        print(tr.__dict__)



def getFiles(myPath):
    all = {}
    files = []
    folders = []
    for (dirpath, dirnames, filenames) in walk(myPath):
        files.extend(addFiles(dirpath, filenames))
    for subfolders in dirnames:
        subs = getFiles(subfolders)
        files.extend(addFiles(dirpath, filename))
    return files


def addFiles(dirpath, files):
    trackfiles = []
    for myFile in files:
        if myFile.endswith(".ogg") or myFile.endswith(".mp3"):
            trackfiles.append(path.join(dirpath, myFile))
    return trackfiles
