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
    # form_data = request.form
    # print(form_data)
    # image_binary = form_data.get('image')
    
    file_storage = request.files['image']
    binary_data = file_storage.read()
    ret = info_generator_interaction(binary_data)
    return jsonify({"message": "Image Uploaded successfully", 'response': ret}), 201


     
