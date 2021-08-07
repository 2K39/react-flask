from flask import Blueprint
from flask_login import LoginManager , login_required , UserMixin
from flask_login import login_user   , current_user , logout_user    
from backend import app , db 
from dataclasses import asdict
from .database import Admin, User

user = Blueprint('user' , __name__)

login_manager =  LoginManager()
login_manager.init_app(app)

@user.route('/view')
def view():
    return asdict(User.query.first())

@login_manager.user_loader
def user_loader(user_id):
    return Admin.query.first()

@user.route('/login')
def login():
    return '200'

@user.route('/logout')
@login_required
def logout():
    logout_user()