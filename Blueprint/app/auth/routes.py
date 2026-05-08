from flask import Blueprint

auth = Blueprint("auth", __name__) # "auth" - Имя Blueprint, Flask использует его внутри системы. 
# __name__ - помогает Flask найти: templates, static файлы, расположение модуля.

@auth.route("/login")              # ВНИМАНИЕ вместо app теперь auth
def login():
    return "Страница логина"

