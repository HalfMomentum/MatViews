from flask import session

def auth(username, password):
    if username == 'Admin' and password == 'Admin':
        try:
            session['auth']=True
        except:
            return False
        return True