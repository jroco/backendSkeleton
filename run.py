from app import create_app
from app.models.user import User
from flask_cors import CORS
import os, logging

app = create_app()
CORS(app)  # Apply CORS to the app

if __name__ == '__main__':
    app.run(host="131.221.33.51",debug=True)