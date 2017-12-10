import os
from flask import jsonify
from flask_restful import Resource
from .vgapi import VaingloryApi

api_key = os.environ.get('API_KEY', None)
api = VaingloryApi(api_key)

class Player(Resource):

    def get(self, player_id, region):
        player = api.player(player_id, region)
        return jsonify(player)

class Players(Resource):

    def get(self, name, region):
        players = api.players([name], region)
        return jsonify(players)


class Match(Resource):

    def get(self, match_id, region):
        match = api.match(match_id, region)
        return jsonify(match)

class Matches(Resource):

    def get(self, name, region):
        matches = api.matches(region, player=[name])
        return jsonify(matches)

class Telemetry(Resource):

    def get(self, match_id, region):
        telemetry = api.telemetry(match_id, region)
        return jsonify(telemetry)
