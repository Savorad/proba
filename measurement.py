from app import db
from sqlalchemy import (Column, Integer, Float, String, DateTime)


class Measurement(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    air_quality = db.Column(db.Float, nullable=False)
    humidity = db.Column(db.Float, nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime(timezone=True), nullable=False, server_default='now()')