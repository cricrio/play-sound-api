#!/usr/bin/python3

from flask import json
from flask import Flask
from flask_restful import reqparse, abort, Resource, Api
from flask_cors import CORS, cross_origin

from player_service import Player_Service

app = Flask(__name__)
CORS(app)
api = Api(app)
tracks = []
player_state = {}


parser = reqparse.RequestParser()
parser.add_argument('state')
parser.add_argument('tracks',action='append',type=int)

def abort_if_track_doesnt_exist(track_id):
    if track_id  > len(tracks) - 1:
        abort(404, message="Track {} doesn't exist".format(track_id))

class State(Resource):
    def get(self):
        player_state = player.get_state()
        return {'state' : player_state.state, 'track' : player_state.track }
    def put(self):
        args = parser.parse_args()
        state = args['state']
        if state == 'play':
            print("get play")
            player.play()
        elif state == 'pause':
            player.pause()
        elif state == 'stop':
            player.stop()


api.add_resource(State,'/state')

class Tracks(Resource):
    def get(self):
    	print(tracks)
    	return tracks

api.add_resource(Tracks, '/tracks')

class Queue(Resource):
    def get(self):
        return player.get_queue()
    def put(self):
        args = parser.parse_args()
        tracks = args['tracks']
        for track in tracks:
            player.add_to_queue(track)
        return player.get_queue()

api.add_resource(Queue, '/queue')


if __name__ == "__main__":
    player = Player_Service('musics')
    tracks = player.get_tracks()
    app.run(debug=True)
