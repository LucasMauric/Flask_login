from app import app,db
from flask import render_template,request,redirect,url_for,flash
from app.models.forms import LoginForm
from app.models.tables import User
from flask_login import LoginManager,current_user,logout_user

login_manager = LoginManager(app)



@login_manager.user_loader
def user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/cadastro",methods = ['GET','POST'])
def cadastro():
    
    if request.method == 'POST':
        username = request.form.get("username")
        name = request.form.get("name")
        passowrd = request.form.get("password")
        email = request.form.get("email")

        usuario = User(username,passowrd,name,email)
        if usuario.username == User.query.filter_by(username = username):
            flash("O nome de usuario ja existe. Por favor, insira outro nome!")
        else:
            flash("Cadastro realizado com sucesso!!!")
            db.session.add(usuario)
            db.session.commit()
     


    return render_template("cadastro.html")



@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))
    


@app.route("/login", methods = ["GET","POST"])
def login():
    form = LoginForm()
    if request.method =='POST':
        user = User.query.filter_by(username = form.username.data).first()
        if form.validate_on_submit():
           if user and user.password == form.password.data:
               flash("Logado com sucesso!!")
               return redirect(url_for("home"))
        else:
            flash("Dados incorretos!!")
        
    return render_template('login.html',form = form)