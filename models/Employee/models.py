from modulo import db

class Employee(db.Model):
    __tablename__ = 'employees'
    employee_id = db.Column("id", db.Integer, primary_key = True )
    employee_name = db.Column(db.String(100), nullable=False)
    employee_mobile = db.Column(db.String(100))
    employee_email = db.Column(db.String(100),nullable=False, unique=True)
    employee_username = db.Column(db.String(200),nullable=False, unique=True)
    employee_password = db.Column(db.String(100),nullable=False)
    employee_adress = db.Column(db.String(100))

    def addEmployee(self, kargs):#Create
        self.employee_name = kargs.get("employee_name", "None")
        self.employee_mobile = kargs.get("employee_mobile", "None")
        self.employee_email = kargs.get("employee_email", "None")
        self.employee_username = kargs.get("employee_username", "None")
        self.employee_password = kargs.get("employee_password", "None")
        self.employee_adress = kargs.get("employee_adress", "None")
        db.session.add(self)
        db.session.commit()

    def editEmployee(self,kargs):#Update
        self.query.filter_by(employee_id=kargs.get("employee_id", "0")).first()
        self.employee_name = kargs.get("employee_name", "None")
        self.employee_mobile = kargs.get("employee_mobile", "None")
        self.employee_email = kargs.get("employee_email", "None")
        self.employee_username = kargs.get("employee_username", "None")
        self.employee_password = kargs.get("employee_password", "None")
        self.employee_adress = kargs.get("employee_adress", "None")
        db.session.commit()

    def deleteEmployee(self):#delete
        db.session.delete(self)
        db.session.commit()
        
    def searchEmployee(self, pk):#read
        return self.query.filter_by(employee_id=pk).first()

    def __repr__(self):
        return "<Name: {}>".format(self.employee_name)