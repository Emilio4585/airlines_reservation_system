from modulo import db

class Passenger(db.Model):
    __tablename__ = 'passengers'
    passenger_id = db.Column("id", db.Integer, primary_key = True, )
    passenger_name = db.Column(db.String(100), nullable=False)
    passenger_mobile = db.Column(db.String(100))
    passenger_email = db.Column(db.String(100),nullable=False, unique=True)
    passenger_username = db.Column(db.String(200),nullable=False, unique=True)
    passenger_password = db.Column(db.String(100),nullable=False)
    passenger_adress = db.Column(db.String(100))

    def addPassenger(self, kargs):#Create
        self.passenger_name = kargs.get("passenger_name", "None")
        self.passenger_mobile = kargs.get("passenger_mobile", "None")
        self.passenger_email = kargs.get("passenger_email", "None")
        self.passenger_username = kargs.get("passenger_username", "None")
        self.passenger_password = kargs.get("passenger_password", "None")
        self.passenger_adress = kargs.get("passenger_adress", "None")
        db.session.add(self)
        db.session.commit()

    def editPassenger(self,kargs):#Update
        self.query.filter_by(passenger_id=kargs.get("passenger_id", "0")).first()
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
        
    def searchPasseger(self, pk):#read
        return self.query.filter_by(passenger_id=pk).first()

    def __repr__(self):
        return "<Name: {}>".format(self.passenger_name)