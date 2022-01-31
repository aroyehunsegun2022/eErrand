from types import MethodType
from urllib import response
from flask import render_template,url_for,session, redirect,request
from itsdangerous import json
from projectapp.myroutes import  user
from projectapp import app,csrf, db
from projectapp.forms import logins, registration
from projectapp.mymodel import signups
from werkzeug.security import check_password_hash, generate_password_hash
import urllib.request, json
import os
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

@app.route('/')
@app.route('/user/home', methods=['POST', 'GET'])
def signup():
    form= registration(request.form)
    hashed=generate_password_hash(form.passwords.data)
    if request.method == 'POST' and form.validate_on_submit:
        userss = signups(signup_email=form.emails.data,signup_fullname=form.fullname.data, signup_passwords=hashed)
        db.session.add(userss)
        db.session.commit()
        return redirect(url_for('signup'))
    return render_template('user/index.html', form=form)




@app.route('/user/viewapi', methods=['POST','GET'])
def get_movies():

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
    'start':'1',
    'limit':'5000',
    'convert':'USD'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
  




@app.route('/user/profile', methods=['POST','GET'])
def profile():
    return render_template('/user/profile.html')

@app.route('/user/profilesubmit', methods=['POST', 'GET'])
def profilesubmit():
    if request.method == 'GET':
        return render_template('/user/index.html/')
    else:
        newfname=request.form.get('pfname')
        newaddress=request.form.get('paddress')
        newphone=request.form.get('paddress')
        newlastname= request.form.get('plastname')
        newstate=request.form.get('pstate')
        newemail=request.form.get('pmail')

    

# @app.route('/user/profile', methods=['POST','GET'])
# def profile():
#     form=updateprofile(request.form)
#     if request.method == 'GET':
#         return render_template('/user/index.html')
#     else: 
#         loginemails=request.form.get('emailupdate')
#         loginpasswords=request.form.get('passwordupdate')
#         loginfullname=request.form.get('fullnameupdate')

#         logon=db.session.query(signups).update(signups.signup_email==loginemails).first()
#         logon=db.session.query(signups).update(signups.signup_fullname==loginfullname).second()
#         if logon:
#             loggedin_user=logon.signup_id
#             formatted=logon.signup_passwords
             
#             confrim=check_password_hash(formatted,loginpasswords)
#             if confrim:
#                 session['user']=loggedin_user
#                 return redirect('/user/dashboard' , form=form  )
#             else:
#                 return 'wrong credentials'
             
#         else:
#             return "invalid credentials"
 


@app.route('/user/login', methods=['POST','GET'])
def login():
    form=logins(request.form)
    if request.method == 'GET':
        return render_template('user/index.html')
    else: 
        loginemails=request.form.get('emails')
        loginpasswords=request.form.get('passwords')
        logon=db.session.query(signups).filter(signups.signup_email==loginemails).first()
        if logon:
            loggedin_user=logon.signup_id
            formatted=logon.signup_passwords
            confrim=check_password_hash(formatted,loginpasswords)
            if confrim:
                session['user']=loggedin_user
                return redirect('/user/dashboard')
            else:
                return 'wrong credentials'
             
        else:
            return "invalid credentials"


# @app.route('/user/login', methods=['POST','GET'])
# def login():
#     form=logins(request.form)
#     if request.method == 'GET':
#         return render_template('index.html')
#     else: 
#         loginemails=request.form.get('emails')
#         loginpasswords=request.form.get('passwords')
#         logon=db.session.query(signup_email=loginemails,signup_passwords=loginpasswords)
#         db.session.query(logon)
#         return render_template('user/dashboard')
         
         
@app.route('/user/dashboard/')
def dashboard():
    loggedin_user=session.get('user')
    if loggedin_user !=None:
        err=db.session.query(signups).get(loggedin_user)
        return render_template('user/dashboard.html', err=err)

# @app.route('/user/profile', methods=['POST','GET'])
# def profile():
#     return render_template('/user/profile.html')


@app.route('/user/layouts/')
def about():
    pwd = app.config['PASSWORD']
    return render_template('user/about.html',pwd=pwd)

@app.route('/contactus/')
def contactus():
    return render_template('user/contactus.html')

@app.route('/about us/')
def aboutus():
    return render_template('user/contactus.html')

@app.route('/whatwedo/')
def whatwedo():
    return render_template('user/contactus.html')


