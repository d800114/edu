from flask import Flask
app = Flask(__name__)
from myapp import views

app.config.from_object('config.DevelopmentConfig') 