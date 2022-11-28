from flask import Flask, session, Blueprint
from user.api import user
from chatbot.api import chatbot

def create_app():
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False

    return app



app = create_app()



@app.route("/")
def hello():
    return "Hello, World!"



app.register_blueprint(user, url_prefix="/user")
app.register_blueprint(chatbot, url_prefix="/chatbot")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)