# Blueprints 
"""
Когда проект становится большим, routes начинают превращаться в хаос.
Blueprint помогает разделять проект на части.

Blueprint - это модуль routes.
Можно разделять проект по частям:
Blueprint	    За что отвечает
auth	        авторизация
blog	        блог
api	            API
admin	        админка

Структура
app/
│
├── auth/
│   ├── __init__.py
│   └── routes.py
│
├── blog/
│   ├── __init__.py
│   └── routes.py
│
├── __init__.py
└── run.py

Идея: КАЖДЫЙ МОДУЛЬ ХРАНИТ СВОЙ ROUTES


"""