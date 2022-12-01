from flask import Blueprint, request, session
from utils.transaction_executor import TransactionExecutor
from utils.jwt_handle import make_jwt_token
from utils.validator import Validator
from chatbot.core import get_response

user = Blueprint("user", __name__)
import hashlib

@user.route("/")
def index():
    return "Hello user"

@user.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user_id = data["userID"]
    password = data["password"]

    return_json = {"success": 0, "msg": ""}

    validator = Validator()
    validator.required([user_id, password])
    validator.check_user_id(user_id)
    validator.check_password(password)
    errors = validator.get_errors()

    if len(errors) != 0:
        return_json["msg"] = errors[0]
        return return_json

    with TransactionExecutor() as transaction_executor:
        """
        Check whether User ID exists in database and get salt, password
        """
        success_flag, result = transaction_executor.query_sql(
            "SELECT salt, password from Users WHERE user_id = %(user_id)s",
            {"user_id": user_id},
            fetch_one=True,
        )
        if success_flag:
            if result == None:
                return_json["msg"] = "User ID doesn't exist"
                return return_json
        else:
            return_json["msg"] = "Server error"
            return return_json

        salt, password_in_database = result
        hash_password = hashlib.pbkdf2_hmac(
            "sha256", password.encode("utf-8"), salt.encode(), 100000
        ).hex()

        if hash_password != password_in_database:
            return_json["msg"] = "Password is wrong"
            return return_json

        if not transaction_executor.commit():
            return_json["msg"] = "SQL Insert error"
            return return_json

        return_json["success"] = 1
        return_json["token"] = make_jwt_token(user_id)
    
    return return_json