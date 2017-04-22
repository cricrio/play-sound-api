#!/usr/bin/python3

from os import walk
from os import path
from tinytag import TinyTag

from models.track import Track

def getAllTracks(myPath):
    i = 0
    trackObjects = []
    tracks = getFiles(myPath)
    for a in tracks:
        tag = TinyTag.get(a,image=True)
        cover_data = tag.get_image()
        if cover_data:
            cover_name = a + '.jpg'
            with open(cover_name,"wb") as f:
                f.write(cover_data)
        trackObjects.append( {'file':a,'id':i,'album':tag.album,'title':tag.title,'artist':tag.artist} )
        i = i+1
    return trackObjects

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
