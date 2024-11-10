# App routes
from flask import Flask, render_template, request
from .models import *
from flask import current_app as app
@app.route('/')
def home():
    
    return render_template('index.html')

@app.route('/login', methods = ["GET", "POST"])
def signin():
    if request.method == "POST":
        uname = request.form.get("user_name")
        pswd = request.form.get("user_password")
        usr = User_Info.query.filter_by(email = uname, password = pswd).first()
        if usr and usr.role == 0: # Existed and admin
            return render_template('admin_dashboard.html')
        elif usr and usr.role == 1: # Existed and normal uer
            return render_template('user_dashboard.html')
        else:
            return render_template('login.html', msg = "Invalid username or password...")
            
    return render_template('login.html', msg = "")

@app.route('/register', methods = ["GET", "POST"])
def signup():
    if request.method == "POST":
        uname = request.form.get("u_name")
        pswd = request.form.get("u_pswd")
        full_name = request.form.get("u_full_name")
        address = request.form.get("u_location")
        pin_code = request.form.get("u_pin")
        usr = User_Info.query.filter_by(email = uname).first()
        if usr:
            return render_template('signup.html', msg = "Sorry, this user already exists...")
        new_usr = User_Info(email = uname, password = pswd, full_name = full_name, address = address, pin_code = pin_code)
        db.session.add(new_usr)
        db.session.commit()
        return render_template('login.html', msg = "Registration Successfully, try login now")
        
    return render_template('signup.html', msg = "")
