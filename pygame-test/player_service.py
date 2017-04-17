#!/usr/bin/python3

import pygame
from trackmanager import getAllTracks
from models.player_state import Player_State

class Player_Service:

    def __init__(self,music_path):
        pygame.init()
        self._tracks = getAllTracks(music_path)
        self._state = Player_State()

    def get_state(self):
        return self._state

    def get_tracks(self):
        return self._tracks

    def play(self,id_track):
        track_path = self._tracks[id_track]['file'] 
        pygame.mixer.music.load(track_path)
        pygame.mixer.music.play(0)
        self._state.setPlay(id_track)

    def stop(self):
        pygame.mixer.music.stop()
        self._state.setStop()

    def pause(self):
        pygame.mixer.music.pause()
        self._state.setPause()
