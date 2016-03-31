class legal_Family_Info(db.model):
    __tablename__ = 'legal_guardian_and_family_info'
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id), unique=True, nullable=False)
    guardian_name = db.Column(db.String)
    guardian_phone = db.Column(db.String)
    guardian_address = db.Column(db.String)
    father_name = db.Column(db.String)
    father_birthday = db.Column(db.Date)
    father_birthplace = db.Column(db.String)
    father_alive = db.Column(db.Boolean)
    mother_maiden_name = db.Column(db.String)
    mother_birthday = db.Column(db.Date)
    mother_birthplace = db.Column(db.String)
    mother_alive = db.Column(db.Boolean)
    parents_martial_status = db.Column(db.String)
    family_phone = db.Column(db.String(10))
    family_address = db.Column(db.String)

