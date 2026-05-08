# Routes (маршруты)
# Route связывает URL и Python функцию.
from flask import Flask

app = Flask(__name__)

@app.route("/")                 # Если пришёл запрос на /, вызови функцию ниже.
def home():                     # Обработчик страницы.
    return "Главная страница"   # Ответ браузеру.

"""
Пользователь открывает:
http://127.0.0.1:5000/
Flask:
получает request
ищет route /
находит home()
запускает функцию
отправляет response
"""

# Можно делать несколько страниц

@app.route("/")
def home():
    return "Главная"

@app.route("/about")
def about():
    return "О нас"

@app.route("/contact")
def contact():
    return "Контакты"

# ВАЖНО URL Должен быть уникальным. Не может быть двух @app.route("/")  @app.route("/")

# Route с параметром
@app.route("/user/<name>")
def user(name):
    return f"Hello, {name}"

# <name> - это переменная внутри URL.
