import os
from datetime import timedelta

from flask import Blueprint, Flask, session
from flask_cors import CORS

import utils.connection_pool as connection_pool
from chatbot.api import chatbot
from user.api import user


def create_app():
    app = Flask(__name__)
    CORS(app, supports_credentials=True)
    app.config["JSON_AS_ASCII"] = False
    app.config["SECRET_KEY"] = os.urandom(24)
    app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(days=3)

    connection_pool.init()

    return app


app = create_app()


@app.before_request
def make_session_permanent():
    session.permanent = True


@app.route("/")
def hello():
    return "Hello, World!"


app.register_blueprint(user, url_prefix="/user")
app.register_blueprint(chatbot, url_prefix="/chatbot")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
