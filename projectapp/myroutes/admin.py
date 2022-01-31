from flask import render_template,url_for,session

from projectapp import app

@app.route('/admin')
def adminhome(): 
    return "Welcome to Admin Home Page"

@app.route('/login')
def adminabout(): 
    return render_template('admin/adminpage.html')