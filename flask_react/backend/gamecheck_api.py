from flask import Blueprint
from flask import Flask, request, jsonify
from utils.database.firebase_api import Firebase
from flask_cors import CORS

api = Flask(__name__)
CORS(api)

gamecheck_api = Blueprint('gamecheck_api', __name__)


@gamecheck_api.route('/judgment', methods=['POST'])
def gamecheck():
    # {'username': 'jackson', 'answer': 'A'}
    data = request.get_json()

    username = data['username']
    answer = data['answer']

    data_processor = Firebase()
    user_answer = data_processor.retrieve_answer(username)['answer']

    user_score = int(data_processor.retrieve_user_score(username))

    if answer == user_answer:
        user_score += 3
        # 学院加分
        data_processor.insert_user_score(username, user_score)
        return jsonify({"message": "Answer correct"}), 201
    else:
        data_processor.insert_user_score(username, user_score)
        return jsonify({"message": "Answer incorrect"}), 201





if __name__ == '__main__':
    api.run(debug=True)

