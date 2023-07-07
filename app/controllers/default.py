from app import app
from flask import render_template,request
from app.models.forms import LoginForm








@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods = ["GET","POST"])
def login():
    form = LoginForm()
    if request.method =='POST':
        if form.validate_on_submit():
            print(form.username.data)
            print(form.password.data)
        else:
            print(form.errors)
        
    return render_template('login.html',form = form)