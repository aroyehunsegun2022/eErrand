#This file will import all the things we need in this package so that it #will be assessible to any module in the package, any module can import as #from thispackage import xx '''

from flask import Flask

from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__,instance_relative_config=True)

csrf = CSRFProtect(app)  #or use this method csrf.init_app(app)

#load the package's config here after the app has been created

from projectapp import config #config within package folder
app.config.from_object(config.LiveConfig)
app.config.from_pyfile('config.py') #loads config from instance folder
db = SQLAlchemy(app)

#Routes are now separated, load routes each from the respective folder
from projectapp.myroutes import admin, user

from projectapp import forms
from projectapp import mymodel
from projectapp import myroutes
