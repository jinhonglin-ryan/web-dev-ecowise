from flask import Blueprint
from flask import Flask, request, jsonify
from utils.database.firebase_api import Firebase
from flask_cors import CORS

api = Flask(__name__)
CORS(api)

login_api = Blueprint('login_api', __name__)

@login_api.route('/login', methods=['POST'])
def login():
    
    data = request.get_json()
    
    username = data['username']
    password = data['password']

    data_processor = Firebase()
    user_password = data_processor.retrieve_user_info(username)['password']

    if password == user_password:
        return jsonify({"message": "Login in successfully"}), 201
    else:
        return jsonify({"message": "User password incorrect"}), 201


if __name__ == '__main__':
    api.run(debug=True)