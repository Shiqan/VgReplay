from flask import Flask, render_template, jsonify
from random import *
from flask_restful import Api
from flask_cors import CORS
import requests

from backend import *

app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")
api = Api(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

api.add_resource(Player, '/api/v1/player/<string:region>/<string:player_id>')
api.add_resource(Players, '/api/v1/players/<string:region>/<string:name>')
api.add_resource(Match, '/api/v1/match/<string:region>/<string:match_id>')
api.add_resource(Matches, '/api/v1/matches/<string:region>/<string:name>')
api.add_resource(Telemetry, '/api/v1/telemetry/<string:region>/<string:match_id>')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")
