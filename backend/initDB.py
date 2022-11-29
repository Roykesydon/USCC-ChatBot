import pymysql
import yaml

with open('config.yml', 'r') as f:
    cfg = yaml.safe_load(f)

connection = pymysql.connect(host=cfg['db']['host'],user=cfg['db']['user'],password=cfg['db']['password'],db=cfg['db']['database'],charset='utf8mb4')

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS user;")
connection.commit()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS user( \
        user_ID varchar(50) NOT NULL, \
        password varchar(70) NOT NULL, \
        PRIMARY KEY (user_ID) \
    );")
connection.commit()