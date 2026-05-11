# Работает по схеме Request → Server → Response
"""
Request — это запрос от клиента к серверу.
Клиентом может быть:
                    браузер,
                    мобильное приложение,
                    frontend,
                    API клиент.
Request хранит:

URL,
метод,
данные формы,
JSON,
headers,
cookies,
query параметры.
"""
#**************************************************
"""
Response — ответ сервера.
Сервер отправляет:
текст,
HTML,
JSON,
файл,
статус код.

CХЕМА:
        Browser
        ↓ request
        Flask
        ↓
        Route
        ↓
        Function
        ↓ response
        Browser
"""
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/search")
def search():

    q = request.args.get("q")

    print(q)

    return f"Поиск: {q}"

app.run(debug=True)

"""
Request.args
Получение query параметров из URL.

Пример URL
/search?q=python

Что такое ?q=python
Это query parameter.


"""
