from flask import Blueprint
from flask import Flask, request
from utils.database.firebase_api import Firebase
from flask_cors import CORS
from utils.bots.game_bot import game_bot_interaction

api = Flask(__name__)
CORS(api)
game_init_api = Blueprint('game_init_api', __name__)

@game_init_api.route('/game_init', methods=['POST'])
def game_init():
    data = request.get_json()

    # Access the 'username' and 'signal' fields from the JSON data
    user_id = data.get('username')
    signal = data.get('signal')

    data_processor = Firebase()
    keyword = data_processor.retrieve_image_label(user_id)

    if (signal == "yes"):
        ret = game_bot_interaction(keyword)
        user_answer = ret["answer"]
        user_answer_dict = {"answer": user_answer}
        data_processor = Firebase()
        data_processor.insert_answer(user_id, user_answer_dict)
        data = {"question": ret["question"], "choices": ret["choices"]}
        return data