from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField
from wtforms.validators import DataRequired



class LoginForm(FlaskForm):
    username = StringField('username',validators=[DataRequired()])
    password = PasswordField('passowrd',validators=[DataRequired()])
    remember_me = BooleanField('remember_me')