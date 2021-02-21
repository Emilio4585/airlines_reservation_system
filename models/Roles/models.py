from modulo import db

<<<<<<< HEAD
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
=======
class Role(db.Model):
    role_id = db.Column("id", db.Integer, primary_key = True, )
    role_title = db.Column(db.String(100))
    role_description = db.Column(db.String(100))


    def addRole(self, aid): # Add a role
        self.role_id = aid.get("role_id", "None")
        self.role_title = aid.get("role_name", "None")
        self.role_description = aid.get("role_description", "None")
        db.session.add(self)
        db.session.commit()

    def editRole(self, ad): # Edit Role
        self.query.filter_by(role_id=ad).first()
        self.role_id = ad.get("role_id", "None")
        self.role_title = ad.get("role_name", "None")
        self.role_description = ad.get("role_description", "None")
        db.session.add(self)
        db.session.commit()

    def deleteRole(self, ai): # Delete a role
        self.query.filter_by(role_id=ai).first()
        self.session.delete()
        self.session.commit()

    def searchRole(self, eid): # Search for a role
        return self.query.filter_by(role_id=eid).first()
        
    def assignRole(self, ed):
        self.role_id = ed.get("role_id", "None")
        self.role_title = ed.get("role_name", "None")
        self.role_description = ed.get("role_description", "None")
        db.session.commit()
>>>>>>> 414c2095997984d143341a9f62ef46ad0e3c719b

    def __repr__(self):
        return "<Name: {}>".format(self.passenger_name)