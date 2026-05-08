"""
Файл routes.py - лежат все routes.
"""
from app import app

@app.route("/")
def home():
    return "Главная страница"