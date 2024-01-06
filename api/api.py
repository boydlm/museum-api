# import os
# import requests
# from flask import Flask, make_response
# from dotenv import load_dotenv
# from api.services import museum_factory
# from api.constants.museum_types import MuseumTypes
# from api.constants.museum_request_types import MuseumRequestTypes

# app = Flask(__name__)
# load_dotenv()
# print(os.getenv("HARVARD_API_KEY"))

# @app.route('/exhibitions/<museum_name>')
# def get_current_exhibitions(museum_name):
#     if museum_name == MuseumRequestTypes.Harvard.value:
#         service = museum_factory.create_museum(MuseumTypes.Harvard.value)
#         exhibitions, errors = service.get_exhibitions()
#         if errors:
#             return make_response("server error", 500)
#         return make_response(exhibitions, 200)

from flask import Flask
from api.container import Container
from api.routes.exhibitions import get_current_exhibitions
from dotenv import load_dotenv

load_dotenv()

def create_app() -> Flask:
    container = Container()
    container.config.harvard_apikey.from_env("HARVARD_API_KEY")

    app = Flask(__name__)
    app.container = container
    app.add_url_rule ('/exhibitions/<museum_name>', "get_current_exhibitions", get_current_exhibitions) 
    
    return app