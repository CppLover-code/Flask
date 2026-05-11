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
from flask import request


