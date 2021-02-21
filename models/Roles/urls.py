from flask import Flask, render_template, flash, request, redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from models.Roles.models import Role
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
def new_Rol():
    if request.method == "POST":
        try:
            role = Role().addRole(request.form)
        except Exception as e:
            flash("There was a failure adding the user try again")
            print("Fallo al añadir usuario")
            print(e)
    return redirect(url_for('home'))

@app.route("/update/<int:qs>", methods=['POST','GET'])
def update_Role(qs):
    if request.method == "POST":
        try:
            rol = Role().assignRole(qs)
        except Exception as e:
            flash("There was a failure to update the role try again")
            print("Fallo al actualizar el role")
            print(e)
    return redirect(url_for("home"))

@app.route("/delete/<int:ai>")
def delete_role(ai):
    if request.method == "POST":
        try:
            bye = Role().deleteRole(ai)
        except Exception as e:
            flash("There was a failure yo delete the role please try again.")
            print("Fallo eliminar el rol")
            print(e)
    return redirect(url_for('home'))

@app.route("/search/<int:ui>")
def searchRole(ui):
    role = Role().searchRole(ui)
    return render_template('info_passenger.html'), role=role)