#!/usr/bin/python3

import pyglet
pyglet.options['audio'] = ('pulse', 'silent')
from trackmanager import getAllTracks
from models.player_state import Player_State





class Player_Service:

    def __init__(self,music_path):
        self._player = pyglet.media.Player()
        self._queue = []
        self._tracks = getAllTracks(music_path)
        self._state = Player_State()

    def get_state(self):
        return self._state

    def get_tracks(self):
        return self._tracks
   
    def get_queue(self):
        return self._queue

    def add_to_queue(self,id_track):
        song = pyglet.media.load(self._tracks[id_track]['file'], streaming=False)
        self._player.queue(song)
    
    def play(self):
        self._player.play()
    
    def pause(self):
        self._player.pause()
        self._state.setPause()
