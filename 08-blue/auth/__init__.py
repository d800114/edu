from flask import Blueprint
auth = Blueprint('auth', __name__, template_folder='templates')

#deepseek
from . import views  # Импортируем views ПОСЛЕ создания blueprint

# работает по: http://127.0.0.1:5000/auth/login