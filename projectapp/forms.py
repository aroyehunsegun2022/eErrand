import email, email_validator
from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired, Email, Length




class registration(FlaskForm):
    emails = StringField('Email:', validators = [Email()])
    fullname = StringField('Your fullname', validators=[DataRequired(), Length(min=4, max=10)])
    passwords= StringField('Your Password', validators=[DataRequired(), Length(min=5, max=15)])

class logins(FlaskForm):
    emails=StringField('Email:', validators = [Email()])
    passwords= StringField('Your Password', validators=[DataRequired(), Length(min=5, max=15)])

# class updateprofile(FlaskForm):
#     emailupdate = StringField('Email:', validators = [Email()])
#     fullnameupdate = StringField('Your fullname', validators=[DataRequired(), Length(min=4, max=10)])
 