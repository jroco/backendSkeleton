from flask import Blueprint, jsonify, request

product_bp = Blueprint('product', __name__)

@product_bp.route('/', methods=['GET'])
def get_products():
    return jsonify({"message": "Lista de productos"})

@product_bp.route('/<id>', methods=['GET'])
def get_product(id):
    return jsonify({"message": f"Detalle del producto {id}"})