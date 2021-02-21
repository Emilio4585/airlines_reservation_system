from modulo import db

class Permission(db.Model):
    permission_id = db.Column("id", db.Integer, primary_key = True)
    permission_role_id = db.Column(db.Integer)
    permission_title = db.Column(db.String(100))
    permission_module = db.Column(db.String(200))
    permission_description = db.Column(db.String(100))


    def addPermission(self, aid): # Add a permission
        self.permission_id = aid.get("permission_id", "None")
        self.permission_title = aid.get("permission_name", "None")
        self.permission_description = aid.get("permission_description", "None")
        db.session.add(self)
        db.session.commit()

    def editPermission(self, ad): # Edit permission
        self.query.filter_by(permission_id=ad).first()
        self.permission_id = ad.get("permission_id", "None")
        self.permission_title = ad.get("permission_name", "None")
        self.permission_description = ad.get("permission_description", "None")
        db.session.add(self)
        db.session.commit()

    def deletePermission(self, ai): # Delete a permission
        self.query.filter_by(permission_id=ai).first()
        self.session.delete()
        self.session.commit()

    def searchPermission(self, eid): # Search for a permission
        return self.query.filter_by(permission_id=eid).first()
        
    def assignPermission(self, ed): # update a permission
        self.permission_id = ed.get("permission_id", "None")
        self.permission_title = ed.get("permission_name", "None")
        self.permission_description = ed.get("permission_description", "None")
        db.session.commit()
