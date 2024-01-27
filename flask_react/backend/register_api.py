from flask import Blueprint
from flask import Flask, request, jsonify
from utils.database.firebase_api import Firebase
from flask_cors import CORS

api = Flask(__name__)
CORS(api)

register_api = Blueprint('register_api', __name__)

@register_api.route('/register', methods=['POST'])
def register():

    data = request.get_json()

    # 数据验证（这里应有更复杂的验证逻辑）
    if 'username' not in data or 'password' not in data:
        return jsonify({"error": "Lack of needed info"}), 400

    # 假设我们在这里将数据存储到数据库
    data_processor = Firebase()
    data_processor.insert_user_info(data)

    # 返回成功响应
    return jsonify({"message": "User register successfully"}), 201


if __name__ == '__main__':
    api.run(debug=True)