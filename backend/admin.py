from .user import login_manager
from backend import db 
from .database import Admin
from flask import Blueprint , render_template , redirect
from flask_login import login_required , current_user , logout_user , login_user
from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField
from wtforms.validators import DataRequired
import bcrypt


admin = Blueprint('admin', __name__ , url_prefix='/admin')


@admin.route('/' ,  methods=['GET', 'POST'])
@login_required
def admin_page():
    return 'hello admin! nice to meet you !' 

class admin_login_form(FlaskForm):
    username = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])

@login_manager.unauthorized_handler
def admin_log():
    return redirect('login')

@admin.route('/login' ,  methods=['GET', 'POST'] )
def admin_login():
    admin_profile = Admin.query.first()
    admin_db_password = admin_profile.password
    form = admin_login_form()
    if form.validate_on_submit():
        print(admin_profile)
        if bcrypt.checkpw(form.username.data.encode() ,  admin_db_password):
            login_user(admin_profile)
            return redirect('/admin')
    return render_template('admin.html' , form = form)

@admin.route('/logout')
def admin_logout():
    logout_user()
    return 'logged out'