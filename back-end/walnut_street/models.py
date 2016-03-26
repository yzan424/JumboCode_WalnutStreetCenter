from flask.ext.sqlalchemy import SQLAlchemy

from . import app


db = SQLAlchemy(app)

ProgramPatient = db.Table(
    'program_patient',
    db.Model.metadata,
    db.Column('patient_id', db.Integer, db.ForeignKey("patient.id")),
    db.Column('program_id', db.Integer, db.ForeignKey("program.id"))
)

class Patient(db.Model):
    
    __tablename__ = 'patient'
    id = db.Column(db.Integer, primary_key=True)

    program = db.relationship(
        'Program',
        secondary=ProgramPatient,
        backref='patients',
    )
    primary_physician_id = db.Column(db.Integer, db.ForeignKey('doctor.id'), unique=True)

    """ Many-one relations """
#    contacts = db.relationship(
#        "Contact",
#        backref='patient')

    """ Unique one-to-one relations """
    basic_info_id = db.Column(db.Integer, db.ForeignKey('basic_info.id'))
    basic_info = db.relationship(
        'BasicInfo',        
        uselist=False, backref='patient'
    )

#;
class BasicInfo(db.Model):

    __tablename__ = 'basic_info'
    id = db.Column(db.Integer, primary_key=True)
    state_id = db.Column(db.String)
    name_first = db.Column(db.String)
    name_last = db.Column(db.String)
    name_preferred = db.Column(db.String)
    birthday = db.Column(db.Date)
    birthplace = db.Column(db.String)
    social_security = db.Column(db.String(9))
    citizenship = db.Column(db.String)
    phone = db.Column(db.String(10))
    phone_on_entry = db.Column(db.String(10))
    day_service = db.Column(db.Boolean)
    training_program_or_school_address = db.Column(db.String)
    training_program_or_school_phone = db.Column(db.String(10))
    area_office = db.Column(db.String)
    record_location = db.Column(db.String)
    address_current = db.Column(db.String)
    address_former = db.Column(db.String)
    sex = db.Column(db.String)
    race = db.Column(db.String)
    blood_type = db.Column(db.String)
    religion = db.Column(db.String)
    marital_status = db.Column(db.String)
    primary_language = db.Column(db.String)
    height = db.Column(db.Float)
    weight = db.Column(db.Float)
    build = db.Column(db.String)
    hair = db.Column(db.String)
    eyes = db.Column(db.String)
    distinguishing_marks = db.Column(db.String)
    competency_status = db.Column(db.String)
    eligibility_date = db.Column(db.Date)
    area_meaningful_tie = db.Column(db.String)
    referral_source = db.Column(db.String)
    accompanied_by = db.Column(db.String)
    work_phone = db.Column(db.String(10))
    work_address = db.Column(db.String)
#;

#TODO: change things like bloodtype, sex, most things to enum. want to be able to change all at once.
#;
class Contact(db.Model):
    __tablename__ = 'contact'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
    patient = db.relationship(
        "Patient",
        primaryjoin='Contact.patient_id==Patient.id',
        backref="contacts"
    )
    relation = db.Column(db.String)
    address = db.Column(db.String)
    date_added = db.Column(db.Date)
    date_removed = db.Column(db.Date)
    removal_reason = db.Column(db.String)
    primary_contact = db.Column(db.Boolean)
#;


class Program(db.Model):
    __tablename__ = 'program'
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String, nullable=False)
#    patients = db.relationship(
#        "patient", back_populates="program")
#    staff = relationship("staff", back_populates="program")
#;

class Staff(db.Model):
    __tablename__ = 'staff'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
#    director_id = Column(Integer, ForeignKey('director.id'))
#    director = relationship("director", back_populates="staff")
    position = db.Column(db.String)
    program_id = db.Column(db.Integer, db.ForeignKey('program.id'))
    program = db.relationship(
        "Program",
        primaryjoin='Staff.program_id==Program.id',
        backref="staff"
    )
    address = db.Column(db.String)
    phone = db.Column(db.String(10))
#;

class Doctor(db.Model):

    __tablename__ = 'doctor'
    id = db.Column(db.Integer, primary_key=True)
    name_full = db.Column(db.String)
    specialization = db.Column(db.String)
    address = db.Column(db.String)
    phone = db.Column(db.String(10))
    fax = db.Column(db.String(10))
    patients = db.relationship(
        "Patient",
        backref="doctors"
    )
