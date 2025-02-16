# backendSkeleton

# Estructura del proyecto:
project/
│
├── app/
│   ├── __init__.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── product_routes.py
│   │   ├── user_routes.py
│   │   └── order_routes.py
│   └── models/
│       ├── __init__.py
│       ├── product.py
│       ├── user.py
│       └── order.py
│
└── run.py
├── README.md

# app/__init__.py
from flask import Flask
from app.routes.product_routes import product_bp
from app.routes.user_routes import user_bp
from app.routes.order_routes import order_bp

def create_app():
    app = Flask(__name__) 
    # Registrar los blueprints
    app.register_blueprint(product_bp, url_prefix='/products')
    app.register_blueprint(user_bp, url_prefix='/users')
    app.register_blueprint(order_bp, url_prefix='/orders')
    return app

# app/routes/product_routes.py
from flask import Blueprint, jsonify, request

product_bp = Blueprint('product', __name__)

@product_bp.route('/', methods=['GET'])
def get_products():
    return jsonify({"message": "Lista de productos"})

@product_bp.route('/<id>', methods=['GET'])
def get_product(id):
    return jsonify({"message": f"Detalle del producto {id}"})

# app/routes/user_routes.py
from flask import Blueprint, jsonify, request

user_bp = Blueprint('user', __name__)

@user_bp.route('/', methods=['GET'])
def get_users():
    return jsonify({"message": "Lista de usuarios"})

@user_bp.route('/<id>', methods=['GET'])
def get_user(id):
    return jsonify({"message": f"Detalle del usuario {id}"})

# app/routes/order_routes.py
from flask import Blueprint, jsonify, request

order_bp = Blueprint('order', __name__)

@order_bp.route('/', methods=['GET'])
def get_orders():
    return jsonify({"message": "Lista de órdenes"})

@order_bp.route('/<id>', methods=['GET'])
def get_order(id):
    return jsonify({"message": f"Detalle de la orden {id}"})

# server.py
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)