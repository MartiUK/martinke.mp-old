import logging

from flask import Flask, make_response
from flask_bootstrap import Bootstrap
from logging.handlers import RotatingFileHandler
from app.web.views import web as WMod
from app.web.views import nav

app = Flask(__name__)
app.config.from_object('config')
LogHandler = RotatingFileHandler(app.config["LOGDIR"], maxBytes=10000,
                                 backupCount=1)
LogFormatter = logging.Formatter(
    "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")

app.secret_key = app.config["SECRET_KEY"]

LogHandler.setLevel(logging.DEBUG)
LogHandler.setFormatter(LogFormatter)
app.logger.addHandler(LogHandler)
app.register_blueprint(WMod)
Bootstrap(app)
nav.init_app(app)
