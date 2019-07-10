from app import db
from sqlalchemy import (Column, Integer, Float, String, DateTime)


class Measurement(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    air_quality = Column(Float, nullable=False)
    humidity = Column(Float, nullable=False)
    temperature = Column(Float, nullable=False)
    timestamp = Column(DateTime(timezone=True), nullable=False, server_default='now()')