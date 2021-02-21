from modulo import db

class Airlines(db.Model):
    __tablename__ = 'Airlines'
    airlines_id = db.Column("id", db.Integer, primary_key = True, )
    airlines_name = db.Column(db.String(100), nullable=False)
    airlines_mobile = db.Column(db.String(100))
    airlines_email = db.Column(db.String(100),nullable=False, unique=True)
    airlines_username = db.Column(db.String(200),nullable=False, unique=True)
    airlines_password = db.Column(db.String(100),nullable=False)
    airlines_adress = db.Column(db.String(100))

    def addAirlines(self, kargs):#Create
        self.airlines_name = kargs.get("airlines_name", "None")
        self.airlines_mobile = kargs.get("airlines_mobile", "None")
        self.airlines_email = kargs.get("airlines_email", "None")
        self.airlines_username = kargs.get("airlines_username", "None")
        self.airlines_password = kargs.get("airlines_password", "None")
        self.airlines_adress = kargs.get("airlines_adress", "None")
        db.session.add(self)
        db.session.commit()

    def editAirlines(self,kargs):#Update
        self.query.filter_by(passenger_id=kargs.get("airlines_id", "0")).first()
        self.airlines_name = kargs.get("airlines_name", "None")
        self.airlines_mobile = kargs.get("airlines_mobile", "None")
        self.airlines_email = kargs.get("airlines_email", "None")
        self.airlines_username = kargs.get("airlines_username", "None")
        self.airlines_password = kargs.get("airlines_password", "None")
        self.airlines_adress = kargs.get("airlines_adress", "None")
        db.session.commit()

    def deleteAirlines(self):#delete
        db.session.delete(self)
        db.session.commit()
        
    def searchAirlines(self, pk):#read
        return self.query.filter_by(airlines_id=pk).first()

    def __repr__(self):
        return "<Name: {}>".format(self.airlines_name)