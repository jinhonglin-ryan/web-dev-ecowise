from flask import Blueprint
from flask import Flask, request, jsonify
from utils.database.firebase_api import Firebase
from flask_cors import CORS
from utils.bots.info_generator import info_generator_interaction

api = Flask(__name__)
CORS(api)

image_api = Blueprint('image_api', __name__)

@image_api.route('/image_upload', methods=['POST'])
def image_upload():
    # retrieve user info
    user_id = request.form.get('username')
    file_storage = request.files['image']
    
    binary_data = file_storage.read()
    ret = info_generator_interaction(binary_data)
    data = {"image_label": ret[1]}
    data_processor = Firebase()
    data_processor.insert_image_label(user_id, data)

    user_score = int(data_processor.retrieve_college_score(user_id)) + 1
    college_score = int(data_processor.retrieve_college_score(user_id)) + 1

    data_processor.insert_user_score(user_id, user_score)
    data_processor.insert_college_score(user_id, college_score)

    return jsonify({"message": "Image Uploaded successfully", 'response': ret[0]}), 201
     
