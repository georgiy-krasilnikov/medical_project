from db import db

def check_user(dict) -> bool:
    login = dict['login']
    password = dict['password']
    users = list(db.get_users())
    
    for u in users:
        if login == u.login and password == u.password:
            return True

    return False