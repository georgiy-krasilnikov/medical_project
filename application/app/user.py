from db import db
from queries import User

def check_user(dict) -> bool:
    login = dict['login']
    password = dict['password']
    users = list(db.get_users())
    
    for u in users:
        if login == u.login and password == u.password:
            return True

    return False

def register_user(dict):
    user = User(login=dict['login'], password=dict['password'])
    db.create_users(u=user)
