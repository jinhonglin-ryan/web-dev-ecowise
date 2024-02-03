from flask import Blueprint
from flask import Flask, request, jsonify
from utils.database.firebase_api import Firebase
from flask_cors import CORS

api = Flask(__name__)
CORS(api)

game_check_api = Blueprint('game_check_api', __name__)


@game_check_api.route('/game_check', methods=['POST'])
def game_check():
    data = request.get_json()

    username = data['username']
    choice = data['answer']

    data_processor = Firebase()
    user_answer = data_processor.retrieve_answer(username)

    user_score = int(data_processor.retrieve_college_score(username)) + 3
    college_score = int(data_processor.retrieve_college_score(username)) + 3

    if choice == user_answer:
        data_processor.insert_user_score(username, user_score)
        data_processor.insert_college_score(username, college_score)
        return jsonify({"message": "Answer correct (User Score + 3; School Score + 3)"}), 201
    else:
        data_processor.insert_user_score(username, user_score)
        return jsonify({"message": f"Answer incorrect (User Score + 0; School Score + 0). Correct Answer is {user_answer}"}), 201


if __name__ == '__main__':
    api.run(debug=True)

