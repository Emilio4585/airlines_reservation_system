from modulo import db

class Permission(db.Model):
    permission_id = db.Column("id", db.Integer, primary_key = True, )
    permission_role_id = db.Column(db.Integer)
    permission_title = db.Column(db.String(100))
    permission_module = db.Column(db.String(500))
    permission_description = db.Column(db.String(500))


    def addPermission(self, aid): # Add a Permission
        self.permission_id = aid.get("permission_id", "None")
        self.permission_role_id = aid.get("permission_role_id", "None")
        self.permission_title = aid.get("permission_title", "None")
        self.permission_module = aid.get("permission_module", "None")
        self.permission_description = aid.get("permission_description", "None")
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

    def __repr__(self):
        return "<Name: {}>".format(self.passenger_name)