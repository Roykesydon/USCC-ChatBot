import pymysql
import yaml

user_input = input("你確定真的要重新初始化資料庫嗎？確定的話請打：「I'm really super clear what I'm doing」\n")
if user_input != "I'm really super clear what I'm doing":
    print("拒絕初始化資料庫")
    exit(0)

with open("config.yml", "r") as f:
    cfg = yaml.safe_load(f)

connection = pymysql.connect(
    host=cfg["db"]["host"],
    user=cfg["db"]["user"],
    password=cfg["db"]["password"],
    db=cfg["db"]["database"],
    charset="utf8mb4",
)

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS Users;")
connection.commit()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS Users( \
        user_id varchar(50) NOT NULL, \
        password varchar(70) NOT NULL, \
        salt varchar(50) NOT NULL, \
        PRIMARY KEY (user_ID) \
    );"
)
connection.commit()
