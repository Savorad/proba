from flask_restplus import Resource
from measurements_bp import measurement_api
from config import Config
from functools import wraps
from werkzeug.exceptions import Forbidden
from flask import request
from measurements_bp.models import Measurement
from app import db
from schemas import CreateMeasurements
from marshmallow import ValidationError
from clients_bp.models import Client

def authentication_required(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        client = Client.query.filter_by(username = request.authorization['username']).first()

        if not request.authorization:
            raise Forbidden

        if(client != None and client.password == request.authorization['password']):
            return f(*args, **kwargs)
        else:
            raise Forbidden
    return wrapped




@measurement_api.route("/", methods=['POST'])
class MeasurementApi(Resource):

    @authentication_required
    def post(self):

        data = request.get_json()
        

        CreateMeasurements().load(data)
        
        measurement = Measurement(
            air_quality = data['air_quality'],
            humidity = data['humidity'],
            temperature = data['temperature']
        )

        db.session.add(measurement)
        db.session.commit()

        return data


