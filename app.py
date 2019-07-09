import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

if os.environ['ENV_TYPE'] == 'Dev':
    from config.development import Development as config
elif os.environ['ENV_TYPE'] == 'Production':
    from config.production import Production as config

db = SQLAlchemy()

from measurement import Measurement

def create_app(conf):
    app = Flask(__name__)
    app.config.from_object(conf)
    return app

app = create_app(config)

migrate = Migrate(app, db)

@app.route("/")
def hello():
    return "Hello world"