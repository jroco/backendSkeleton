from flask import Blueprint, jsonify, request

order_bp = Blueprint('order', __name__)

@order_bp.route('/', methods=['GET'])
def get_orders():
    return jsonify({"message": "Lista de órdenes"})

@order_bp.route('/<id>', methods=['GET'])
def get_order(id):
    return jsonify({"message": f"Detalle de la orden {id}"})