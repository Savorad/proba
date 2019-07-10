from flask_restplus import Resource
from clients_bp import client_api
from functools import wraps
from werkzeug.exceptions import Forbidden
from flask import request
from clients_bp.models import Client
from app import db

@client_api.route("/", methods=['POST'])
class ClientApi(Resource):

    def post(self):

        data = request.get_json()
        
        client = Client(
            username = data['username'],
            password = data['password']
        )

        db.session.add(client)
        db.session.commit()
        
        return data
