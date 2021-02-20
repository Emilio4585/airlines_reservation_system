from modulo import db

class Passenger(db.Model):
    passenger_id = db.Column("id", db.Integer, primary_key = True, )
    passenger_name = db.Column(db.String(100))
    passenger_mobile = db.Column(db.String(100))
    passenger_email = db.Column(db.String(100))
    passenger_username = db.Column(db.String(200))
    passenger_password = db.Column(db.String(100))
    passenger_adress = db.Column(db.String(100))

    def __repr__(self):
        return "<Name: {}>".format(self.passenger_name)