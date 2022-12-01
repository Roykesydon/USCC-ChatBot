

## 事前準備
1. 下載 jieba 正體中文詞庫，並放在 backend 目錄下

    ```
    wget https://raw.githubusercontent.com/fxsjy/jieba/master/extra_dict/dict.txt.big
    ```

2. 填寫 .env

3. 填寫 /backend/config.yml

## 如何使用
```
docker-compose up --build -d
```

第一次開專案可以進去 backend 的 container 執行 init_database.py
把資料庫的 table 設定好
也可去 backend 的 container 跑 create_account.py 來創建網站帳號
因為現在還未規劃好的創帳號方式

## 關閉專案
```
docker-compose down
```