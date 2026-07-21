# в вашем приложении /auth/views.py)
from . import auth

@auth.route('/login', methods= [ 'GET', 'POST'])
def login():
    return "Login Here"

#deepseek
#@auth.route('/')
#def index():
#    return "Auth Index"