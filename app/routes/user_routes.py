from flask import Blueprint, jsonify, request

user_bp = Blueprint('user', __name__)

@user_bp.route('/', methods=['GET'])
def get_users():
    return jsonify({"message": "Lista de usuarios"})

@user_bp.route('/<id>', methods=['GET'])
def get_user(id):
    return jsonify({"message": f"Detalle del usuario {id}"})