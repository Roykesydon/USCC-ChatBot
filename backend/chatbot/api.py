from flask import Blueprint, request, session
from chatbot.core import get_response
from utils.jwt_handle import check_jwt_token_and_get_info

chatbot = Blueprint("chatbot", __name__)


@chatbot.route("/")
def index():
    return "Hello chatbot"


@chatbot.route("/query", methods=["GET"])
def query():
    return_json = {"success": False, "text": "", "msg": ""}
    query = request.args.get("text")
    token = request.headers.get("Authorization").replace("Bearer ", "")

    """
    Check jwt token
    """
    token_parse_result = check_jwt_token_and_get_info(token)
    if not token_parse_result["success"]:
        return_json["msg"] = token_parse_result["msg"]
        return return_json

    """
    Check query text length
    """
    if len(query) > 100:
        return_json["msg"] = "query too long"
        return return_json

    answer = get_response(query)

    return_json["success"] = True
    return_json["text"] = answer

    return return_json
