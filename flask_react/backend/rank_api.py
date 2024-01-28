from flask import Blueprint
from flask import Flask, jsonify, request
from utils.database.firebase_api import Firebase
from flask_cors import CORS

api = Flask(__name__)
CORS(api)

rank_api = Blueprint('rank_api', __name__)


@rank_api.route('/rank_api', methods=['GET'])
def ranking():
    firebase = Firebase()
    return firebase.retrieve_rankedlist()

