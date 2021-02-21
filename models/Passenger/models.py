from modulo import db

class Passenger(db.Model):
    passenger_id = db.Column("id", db.Integer, primary_key = True, )
    passenger_name = db.Column(db.String(100))
    passenger_mobile = db.Column(db.String(100))
    passenger_email = db.Column(db.String(100))
    passenger_username = db.Column(db.String(200))
    passenger_password = db.Column(db.String(100))
    passenger_adress = db.Column(db.String(100))

    def addPassenger(self, kargs):#Create
        self.passenger_id = kargs.get("passenger_id", "None")
        self.passenger_name = kargs.get("passenger_name", "None")
        self.passenger_mobile = kargs.get("passenger_mobile", "None")
        self.passenger_email = kargs.get("passenger_email", "None")
        self.passenger_username = kargs.get("passenger_username", "None")
        self.passenger_password = kargs.get("passenger_password", "None")
        self.passenger_adress = kargs.get("passenger_adress", "None")
        db.session.add(self)
        db.session.commit()

    def editPassenger(self, pk):#Update
        self.query.filter_by(passenger_id=pk).first()
        self.passenger_id = kargs.get("passenger_id", "None")
        self.passenger_name = kargs.get("passenger_name", "None")
        self.passenger_mobile = kargs.get("passenger_mobile", "None")
        self.passenger_email = kargs.get("passenger_email", "None")
        self.passenger_username = kargs.get("passenger_username", "None")
        self.passenger_password = kargs.get("passenger_password", "None")
        self.passenger_adress = kargs.get("passenger_adress", "None")
        db.session.commit()

    def deletePassenger(self):#delete
        db.session.delete(self)
        db.session.commit()
        
    def searchPasseger(self):#read
        pass
    
    def __repr__(self):
        return "<Name: {}>".format(self.passenger_name)