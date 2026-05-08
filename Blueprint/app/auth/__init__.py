from flask import Flask
from app.auth.routes import auth

app = Flask(__name__)
app.register_blueprint(auth) # регистрируем blueprint

# register_blueprint - подключает routes, добавляет URL, начинает их обрабатывать
