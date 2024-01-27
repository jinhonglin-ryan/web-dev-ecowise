from flask import Blueprint
from flask import Flask, request, jsonify
from utils.database.firebase_api import Firebase
from flask_cors import CORS
from utils.bots.info_generator import info_generator_interaction

api = Flask(__name__)
CORS(api)

game_api = Blueprint('game_api', __name__)

@game_api.route('/game/question', methods=['POST'])
def game_question():
    
    return

@game_api.route('/game/answer', methods=['POST'])
def game_answer():
    
    return