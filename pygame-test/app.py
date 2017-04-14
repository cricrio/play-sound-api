#!/usr/bin/python3

import pygame
from flask import json
from flask import Flask
from flask_restful import Resource, Api
from trackmanager import getAllTracks

tracks = []
app = Flask(__name__)
api = Api(app)


class Play(Resource):
    def get(self):
        pygame.mixer.music.load('./musics/02.ogg')
        pygame.mixer.music.play(0)
        return "playing",200


api.add_resource(Play, '/play')


class Stop(Resource):
    def get(self):
    	pygame.mixer.music.stop()
    	return "stoped",200


api.add_resource(Stop, '/stop')


class Tracks(Resource):
    def get(self):
    	print(tracks)
    	return tracks


api.add_resource(Tracks, '/tracks')


if __name__ == "__main__":
    pygame.init()
    tracks = getAllTracks("musics")
    app.run(debug=True)
    print(tracks)
