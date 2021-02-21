from flask import Flask, render_template, flash, request, redirect,url_for
from flask_sqlalchemy import SQLAlchemy
<<<<<<< HEAD
from models import Passenger
=======
from models.Roles.models import Role
>>>>>>> 414c2095997984d143341a9f62ef46ad0e3c719b
from ...modulo import app,db

@app.route("/", methods=["POST", "GET"])
def home():
    users_per_page = 5
    all_data = Role.query.all()
    total_user = len(Role.query.all())
    page = request.args.get('page',1, type =int)
    users = Role.query.paginate(page=page, per_page = users_per_page)
    return render_template("index.html",User = users)

@app.route('/new', methods=["POST", "GET"])
<<<<<<< HEAD
def new_passenger():
    if request.method == "POST":
        try:
            passenger = Passenger().addPassenger(request.form)
=======
def new_Rol():
    if request.method == "POST":
        try:
            role = Role().addRole(request.form)
>>>>>>> 414c2095997984d143341a9f62ef46ad0e3c719b
        except Exception as e:
            flash("There was a failure adding the user try again")
            print("Fallo al añadir usuario")
            print(e)
    return redirect(url_for('home'))

<<<<<<< HEAD
@app.route("/update/<int:pk>", methods=['POST','GET'])
def update_passenger(pk):
    if request.method == "POST":
        try:
            passenger = Passenger().editPassenger(pk)
=======
@app.route("/update/<int:qs>", methods=['POST','GET'])
def update_Role(qs):
    if request.method == "POST":
        try:
            rol = Role().assignRole(qs)
>>>>>>> 414c2095997984d143341a9f62ef46ad0e3c719b
        except Exception as e:
            flash("There was a failure to update the role try again")
            print("Fallo al actualizar el role")
            print(e)
    return redirect(url_for("home"))

<<<<<<< HEAD
@app.route("/delete/<int:pk>")
def delete_passenger(pk):
    passenger = Passenger().deletePassenger(pk)
=======
@app.route("/delete/<int:ai>")
def delete_role(ai):
    if request.method == "POST":
        try:
            bye = Role().deleteRole(ai)
        except Exception as e:
            flash("There was a failure yo delete the role please try again.")
            print("Fallo eliminar el rol")
            print(e)
>>>>>>> 414c2095997984d143341a9f62ef46ad0e3c719b
    return redirect(url_for('home'))

@app.route("/search/<int:pk>")
def search_passenger(pk):
    passenger = Passenger().searchPasseger(pk)
    return render_template('info_passenger.html'), passenger=passenger)