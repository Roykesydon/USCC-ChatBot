from flask import Blueprint, request
from chatbot.core import get_response

chatbot = Blueprint("chatbot", __name__)


@chatbot.route("/")
def index():
    return "Hello chatbot"


@chatbot.route("/query", methods=["GET"])
def query():
    return_json = {"success": False, "text": "", "msg": ""}
    query = request.args.get("text")

    if len(query) > 100:
        return_json["msg"] = "query too long"
        return return_json

    answer = get_response(query)
    # print(answer)

    return_json["success"] = True
    return_json["text"] = answer

    return return_json
