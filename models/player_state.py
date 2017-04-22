#!/usr/bin/python3

class Player_State:
    def __init__(self):
        self._state = 'none'
        self._track = -1
    
    def setPlay(self,id_track):
        self._state = 'playing'
        self._track = id_track
    
    def setPause(self):
        self._state = 'pause'
        
    def setStop(self):
        self._state = 'stop'
        self._track = -1


    @property
    def track(self):
        return self._track

    @property
    def state(self):
        return self._state
