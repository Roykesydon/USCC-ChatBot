from flask import Blueprint, request
from chatbot.core import get_response

chatbot = Blueprint("chatbot", __name__)

@chatbot.route("/")
def index():
    return "Hello chatbot"

@chatbot.route("/query", methods=["GET"])
def query():
    query = request.args.get('text')
    answer = get_response(query)
    # print(answer)

    return_json = {
        "text" : answer
    }

    return return_json