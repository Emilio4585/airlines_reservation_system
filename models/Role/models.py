from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from modulo import db


class Role_model(db.Model): 
    _id = db.Column("id", db.Integer, primary_key = True )
    title = db.Column(db.String(100))
    descriptcion = db.Column(db.String(250))

    def __repr__(self):
        return "<Name: {}>".format(self.name)



class Role():
    pass