from flask import request, jsonify, make_response
from flask_restful import Resource
from app import db
from app.models import Parking
from datetime import datetime

class ParkingResource(Resource):
    def post(self):
        data = request.get_json()
        plate = data.get('plate')

        if not plate:
            return {'message': 'Plate number is required'}, 400

        # Implemente a validação da máscara AAA-9999

        parking = Parking(plate=plate, entry_time=datetime.now())
        db.session.add(parking)
        db.session.commit()

        return {'message': 'Entry registered successfully', 'id': parking.id}, 201

    def put(self, id):
        parking = Parking.query.get(id)

        if not parking:
            return {'message': 'Parking not found'}, 404

        if parking.paid:
            parking.left = True
            db.session.commit()
            return {'message': 'Parking left successfully'}
        else:
            return {'message': 'Payment required before leaving'}, 400


class PaymentResource(Resource):
    def put(self, id):
        parking = Parking.query.get(id)

        if not parking:
            return {'message': 'Parking not found'}, 404

        parking.paid = True
        db.session.commit()

        return {'message': 'Payment accepted'}


class HistoryResource(Resource):
    def get(self, plate):
        parkings = Parking.query.filter_by(plate=plate).all()
        history = [{'id': p.id, 'time': calculate_time(p.entry_time), 'paid': p.paid, 'left': p.left} for p in parkings]
        return history


def calculate_time(entry_time):
    # Implemente o cálculo do tempo decorrido
    return '25 minutes'  # Exemplo
