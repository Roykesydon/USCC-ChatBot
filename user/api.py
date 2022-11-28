from flask import Blueprint

user = Blueprint("user", __name__)

@user.route("/")
def index():
    return "Hello user"

@user.route("/login", methods=["POST"])
def login():
    return_json = {
        "text" : "login success"
    }

    return return_json