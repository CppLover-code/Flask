"""
Самый важный файл структуры:
создаёт Flask app,
настраивает приложение,
подключает routes.
"""

from flask import Flask

app = Flask(__name__)

from app import routes

# ВАЖНО Flask app создаётся ОДИН раз: app = Flask(__name__), 
# потом этот app используется во всех файлах проекта.