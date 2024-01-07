from flask import Flask
from api.container import Container
from api.routes.exhibitions import get_current_exhibitions
from dotenv import load_dotenv
import logging
import sys

load_dotenv()

logging.basicConfig(stream=sys.stdout, level=logging.INFO, encoding="utf-8")
handler = logging.StreamHandler(stream=sys.stdout)
log = logging.getLogger("museum_api")
log.addHandler(handler)
log.propogate = False

def create_app() -> Flask:
    container = Container()
    container.config.harvard_apikey.from_env("HARVARD_API_KEY")

    app = Flask(__name__)
    app.container = container
    app.add_url_rule ('/exhibitions/<museum_name>', "get_current_exhibitions", get_current_exhibitions) 
    
    return app