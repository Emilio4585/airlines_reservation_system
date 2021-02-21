from flask import Flask, render_template, flash, request, redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from models import Permission
from ...modulo import app,db

@app.route("/", methods=["POST", "GET"])
def home():
    users_per_page = 5
    all_data = Permission.query.all()
    total_user = len(Permission.query.all())
    page = request.args.get('page',1, type =int)
    users = Permission.query.paginate(page=page, per_page = users_per_page)
    return render_template("index.html",Permission = users)

@app.route('/new', methods=["POST", "GET"])
def new_Permission():
    if request.method == "POST":
        try:
            Permission = Permission().addPermission(request.form)
        except Exception as e:
            flash("There was a failure adding the Permission try again")
            print("Fallo al añadir usuario")
            print(e)
    return redirect(url_for('home'))

@app.route("/update/<int:pk>", methods=['POST','GET'])
def update_Permission(pk):
    if request.method == "POST":
        try:
            Permission = Permission().editPermission(pk)
        except Exception as e:
            flash("There was a failure to update the Permission try again")
            print("Fallo al actualizar el Permission")
            print(e)
    return redirect(url_for("home"))

@app.route("/delete/<int:pk>")
def delete_Permission(pk):
    Permission = Permission().deletePermission(pk)
    return redirect(url_for('home'))

@app.route("/search/<int:pk>")
def search_Permission(pk):
    Permission = Permission().searchPermission(pk)
    return render_template('info_Permission.html'), Permission=Permission)