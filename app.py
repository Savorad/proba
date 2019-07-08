from flask import Flask
from config.development import Developmnet as config

def create_app(conf):
    app = Flask(__name__)
    app.config.from_object(conf)
    return app

app = create_app(config)

@app.route("/")
def hello():
    return "Hello world"