from modulo import db

class Role(db.Model):
    role_id = db.Column("id", db.Integer, primary_key = True)
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
        
    def assignRole(self, ed): # update a role
        self.role_id = ed.get("role_id", "None")
        self.role_title = ed.get("role_name", "None")
        self.role_description = ed.get("role_description", "None")
        db.session.commit()
<<<<<<< HEAD
=======

    def __repr__(self):
        return "<Name: {}>".format(self.passenger_name)
>>>>>>> main
