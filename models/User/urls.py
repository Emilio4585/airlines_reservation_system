from flask import Flask, render_template, flash, request, redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from models import Passenger
from ...modulo import app,db

@app.route("/", methods=["POST", "GET"])
def home():
    users_per_page = 5
    all_data = User.query.all()
    total_user = len(User.query.all())
    page = request.args.get('page',1, type =int)
    users = User.query.paginate(page=page, per_page = users_per_page)
    return render_template("index.html",User = users)

@app.route('/new', methods=["POST", "GET"])
def new_passenger():
    if request.method == "POST":
        try:
            passenger = Passenger().addPassenger(request.form)
        except Exception as e:
            flash("There was a failure adding the user try again")
            print("Fallo al añadir usuario")
            print(e)
    return redirect(url_for('home'))

@app.route("/update/<int:pk>", methods=['POST','GET'])
def update_passenger(pk):
    if request.method == "POST":
        try:
            passenger = Passenger().editPassenger(pk)
        except Exception as e:
            flash("There was a failure to update the user try again")
            print("Fallo al actualizar el user")
            print(e)
    return redirect(url_for("home"))

@app.route("/delete/<int:pk>")
def delete_passenger(pk):
    passenger = Passenger().deletePassenger(pk)
    return redirect(url_for('home'))

@app.route("/search/<int:pk>")
def search_passenger(pk):
    passenger = Passenger().searchPasseger(pk)
    return render_template('info_passenger.html'), passenger=passenger)