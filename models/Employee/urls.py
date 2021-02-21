from flask import Flask, render_template, flash, request, redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from models import Employee
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
def new_employee():
    if request.method == "POST":
        try:
            employee = Employee().addEmployee(request.form)
        except Exception as e:
            flash("There was a failure adding the user try again")
            print("Fallo al añadir usuario")
            print(e)
    return redirect(url_for('home'))

@app.route("/update/<int:pk>", methods=['POST','GET'])
def update_employee(pk):
    if request.method == "POST":
        try:
            employee = Employee().editEmployee(pk)
        except Exception as e:
            flash("There was a failure to update the user try again")
            print("Fallo al actualizar el user")
            print(e)
    return redirect(url_for("home"))

@app.route("/delete/<int:pk>")
def delete_employee(pk):
    employee = Employee().deleteEmployee(pk)
    return redirect(url_for('home'))

@app.route("/search/<int:pk>")
def search_employee(pk):
    employee = Employee().searchEmployee(pk)
    return render_template('info_employee.html'), employee=employee)