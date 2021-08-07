from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
from backend import config
db = SQLAlchemy(app)

from backend import database
from .routes import router
from .admin  import admin
from .user import user

app.register_blueprint(router)
app.register_blueprint(admin)
app.register_blueprint(user)