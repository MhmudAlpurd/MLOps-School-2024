from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length



class LoginForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired('lotfan username ra vared konid')])
    password = PasswordField(label = 'Password', validators=[DataRequired('lotfan password ra vared konid'), Length(min=2, message='you must enter character more than 2')])
    submit =  SubmitField()
