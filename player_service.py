#!/usr/bin/python3

import pygame
from trackmanager import getAllTracks
from models.player_state import Player_State


SONG_END = pygame.USEREVENT + 1



class Player_Service:

    def __init__(self,music_path):
        pygame.init()
        pygame.mixer.music.set_endevent(SONG_END)
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
        self._queue.append(id_track)
    
    def play_one(self,id_track):
        track_path = self._tracks[id_track]['file']
        pygame.mixer.music.load(track_path)
        pygame.mixer.music.play(0)
        self._state.setPlay(id_track)
    
    def play(self):
        id_track = self._queue.pop(-1)
        self.play_one(id_track)
        while len(self._queue) > 0:
            for event in pygame.event.get():
                if event.type == SONG_END:
                    #pop the last (default)
                    id_track = self._queue.pop(-1)
                    self.play_one(id_track)

    
    def stop(self):
        pygame.mixer.music.stop()
        self._state.setStop()

    def pause(self):
        pygame.mixer.music.pause()
        self._state.setPause()
