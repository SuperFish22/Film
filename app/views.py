from flask import render_template, request,url_for
#from flask_login import login_required
from app import app
from .models import FilmGo,pouisc_Film

@app.route("/")
def index():
    db = FilmGo()
    print(db)
    return render_template('index.html', film_list = db)

@app.route('/fi/<id>')
def film(id):
    db =  pouisc_Film(id)
    print(db)
    return render_template ("film.html",film_list = db)

@app.route("/login")
def login():

    return render_template("login.html")

@app.route("/regis")
def regis():
    return render_template("regis.html")

@app.route("/account")
def account():
    return render_template("acount.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")
