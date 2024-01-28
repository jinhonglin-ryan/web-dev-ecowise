from flask import Flask
from register_api import register_api
from login_api import login_api
from image_api import image_api
from game_init_api import game_init_api
from game_check_api import game_check_api
from rank_api import rank_api


api = Flask(__name__)

api.register_blueprint(register_api)
api.register_blueprint(login_api)
api.register_blueprint(image_api)
api.register_blueprint(game_init_api)
api.register_blueprint(game_check_api)
api.register_blueprint(rank_api)

@api.route('/')
def my_profile():
    response_body = {
        "name": "Nagato",
        "about" :"Hello! I'm a full stack developer that loves python and javascript"
    }

    return response_body


if __name__ == '__main__':
     api.run(debug = True)

