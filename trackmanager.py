#!/usr/bin/python3

from os import walk
from os import path
from tinytag import TinyTag

from models.track import Track


def getAllTracks(myPath):
    i = 0
    track_objects = []
    tracks = getFiles(myPath)
    for track in tracks:
        tag = TinyTag.get(track)
        # if tag.title == Null:
        #     tag.title = a
        # if tag.album == Null:
        #     tag.album = "Inconnue"
        # if tag.artist == Null:
        #     tag.artist = "Inconnue"
        track = {'file': track,
                 'id': i,
                 'album': tag.album,
                 'title': tag.title,
                 'artist': tag.artist}
        track_objects.append(track)
        i = i + 1
    return track_objects


def getFiles(myPath):
    files = []
    for (dirpath, dirnames, filenames) in walk(myPath):
        files.extend(addFiles(dirpath, filenames))
    for subfolders in dirnames:
        subs = getFiles(subfolders)
        files.extend(addFiles(dirpath, subs))
    return files


def addFiles(dirpath, files):
    trackfiles = []
    for my_file in files:
        if my_file.endswith(".ogg") or my_file.endswith(".mp3"):
            trackfiles.append(path.join(dirpath, my_file))
    return trackfiles
