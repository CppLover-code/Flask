from flask import Flask
from app.auth.routes import auth

app = Flask(__name__)

app.register_blueprint(auth)