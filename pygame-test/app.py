#!/usr/bin/python3

import pygame
from flask import json
from flask import Flask
from flask_restful import reqparse, abort, Resource, Api
from trackmanager import getAllTracks


app = Flask(__name__)
api = Api(app)

def abort_if_track_doesnt_exist(track_id):
    if track_id  > len(tracks) - 1:
        abort(404, message="Track {} doesn't exist".format(track_id))

class Play(Resource):
    def get(self,track_id):
        id = int(track_id)
        abort_if_track_doesnt_exist(id)
        print( tracks[id])
        pygame.mixer.music.load(tracks[id]['file'])
        pygame.mixer.music.play(0)
        return "playing",200


api.add_resource(Play, '/play/<track_id>')


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
