#!/usr/bin/python3

from flask import json
from flask import Flask
from flask_restful import reqparse, abort, Resource, Api

from player_service import Player_Service

app = Flask(__name__)
api = Api(app)
tracks = []
player_state = {}


parser = reqparse.RequestParser()
parser.add_argument('state')
parser.add_argument('track')

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
        track_id = args['track']
        if state == 'play':
            id = int(track_id)
            player.play(id)
        elif state == 'pause':
            player.pause()
        elif state == 'stop':
            player.stop()


api.add_resource(State,'/state')

class Play(Resource):
    def get(self,track_id):
        id = int(track_id)
        player.play(id)
        return "playing",200


api.add_resource(Play, '/play/<track_id>')


class Stop(Resource):
    def get(self):
        player.stop()
        return "stoped",200



api.add_resource(Stop, '/stop')


class Tracks(Resource):
    def get(self):
    	print(tracks)
    	return tracks


api.add_resource(Tracks, '/tracks')


if __name__ == "__main__":
    player = Player_Service('musics')
    app.run(debug=True)
