''' This handles database connections'''
import datetime
import enum

from sqlalchemy.orm import backref
from projectapp import db


class signups(db.Model):
    signup_id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    signup_fullname = db.Column(db.String(99), nullable=False)
    signup_email = db.Column(db.String(99), nullable=False)
    signup_passwords = db.Column(db.String(500), nullable=False)
    signup_createdon = db.Column(db.DateTime(), default=datetime.datetime.utcnow)

class Errandverifier(db.Model):
    errandverifier_id= db.Column(db.Integer, primary_key=True, autoincrement=True)
    errandverifier_status=db.Column(db.Enum('Verified', 'Not Verified'))

class Errander(db.Model):
    errander_id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    errander_name = db.Column(db.String(60),nullable=False)
    errander_address = db.Column(db.String(60),nullable=False)
    errander_email = db.Column(db.String(60),nullable=False)
    errander_phone = db.Column(db.Integer,nullable=False)
    errander_gender = db.Column(db.Enum('Male', 'Female'))
    errandverifier_id= db.Column(db.Integer(),db.ForeignKey('errandverifier.errandverifier_id')) 

class Errandee(db.Model):
    errandee_id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    errandee_name = db.Column(db.String(60),nullable=False)
    errandee_address = db.Column(db.String(60),nullable=False)
    errandee_email = db.Column(db.String(60),nullable=False)
    errandee_phone = db.Column(db.Integer,nullable=False)
    errandee_gender = db.Column(db.Enum('Male', 'Female'))
    errander_id = db.Column(db.Integer(), db.ForeignKey('errander.errander_id'))
    errandverifier_id= db.Column(db.Integer(),db.ForeignKey('errandverifier.errandverifier_id'))

class Transactions(db.Model):
    transactions_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    transactions_history = db.Column(db.String(60),nullable=False)
    transactions_status = db.Column(db.Enum('Successful', 'Failed'))
    errander_id = db.Column(db.Integer(), db.ForeignKey('errander.errander_id'))
    errandee_id = db.Column(db.Integer(), db.ForeignKey('errandee.errandee_id'))

class Errands(db.Model):
    errands_id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    errands_status = db.Column(db.Enum('completed', 'Ongoing', 'Rejected', 'Accepted')) 
    errands_type = db.Column(db.Enum('Indoor Errand', 'Outdoor Errand', 'Artisans Errand'))        
 


 