from flask import Flask
from src.utils.custom_log import Logger
from localization.en_contsts import ROUTER_PATHS_ARE_SET, PING_LOG_MSG


app = Flask(__name__)


@app.route('/')
def ping() -> str:
   return PING_LOG_MSG


Logger.log(ROUTER_PATHS_ARE_SET)