from flask import Flask
from register_api import register_api
from login_api import login_api
from image_api import image_api
from game_api import game_api
from gamecheck_api import gamecheck_api


api = Flask(__name__)

api.register_blueprint(register_api)
api.register_blueprint(login_api)
api.register_blueprint(image_api)
api.register_blueprint(game_api)
api.register_blueprint(gamecheck_api)

@api.route('/')
def my_profile():
    response_body = {
        "name": "Nagato",
        "about" :"Hello! I'm a full stack developer that loves python and javascript"
    }

    return response_body


if __name__ == '__main__':
     api.run(debug = True)

