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