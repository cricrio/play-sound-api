#!/usr/bin/python3

class Track(object):
    def __init__(self,file,id):
        self._id = id
        self._file = file

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self,f):
        self._file = f

    @property
    def file(self):
        return self._file

    @file.setter
    def file(self,f):
        self._file = f
