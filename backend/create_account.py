import base64
import hashlib
import os

import utils.connection_pool as connection_pool
from utils.transaction_executor import TransactionExecutor

connection_pool.init()

print("輸入要新增的帳號密碼\n" "請只輸入大小寫英文或數字\n" "User ID 和密碼的長度請輸入 3 ~ 30 個字元")
user_id = input("請輸入要新增的 User ID: ")
user_password = input("請輸入要新增的 User Password: ")

with TransactionExecutor() as transaction_executor:
    """
    Check whether user_id already been used or not
    """
    success_flag, result = transaction_executor.query_sql(
        "SELECT * from Users WHERE user_id = %(user_id)s",
        {"user_id": user_id},
        fetch_one=True,
    )

    if success_flag:
        if result != None:
            print("Email already been used")
            exit(0)
    else:
        print("server error")
        exit(0)

    """
    Insert user information into database
    """
    salt = os.urandom(16)
    salt = base64.b64encode(salt)

    hash_password = hashlib.pbkdf2_hmac(
        "sha256", user_password.encode("utf-8"), salt, 100000
    ).hex()

    insert_string = "INSERT INTO Users(user_id, salt, password) values (%(user_id)s, %(salt)s, %(password)s)"
    success_flag = transaction_executor.execute_sql(
        insert_string,
        {
            "name": None,
            "user_id": user_id,
            "salt": salt,
            "password": hash_password,
        },
    )
    if not success_flag:
        print("server error")
        exit(0)

    if not transaction_executor.commit():
        print("SQL Insert error")
        exit(0)

print("註冊成功")
