from flask.ext.sqlalchemy import SQLAlchemy

from . import app


db = SQLAlchemy(app)


ProgramPatient = db.Table(
    'program_patient',
    db.Model.metadata,
    db.Column('patient_id', db.Integer, db.ForeignKey("patient.id")),
    db.Column('program_id', db.Integer, db.ForeignKey("program.id"))
)


DoctorPatient = db.Table(
    'doctor_patient',
    db.Model.metadata,
    db.Column('patient_id', db.Integer, db.ForeignKey("patient.id")),
    db.Column('doctor_id', db.Integer, db.ForeignKey("doctor.id"))
)


class Patient(db.Model):

    __tablename__ = 'patient'
    id = db.Column(db.Integer, primary_key=True)

    name_first = db.Column(db.String)
    name_last = db.Column(db.String)

    """ Many-to-many relations """
    program = db.relationship(
        'Program',
        secondary=ProgramPatient,
        backref='patients',
    )
    primary_physician_id = db.Column(db.Integer, db.ForeignKey('doctor.id'), unique=True)
    primary_physician = db.relationship(
        'Doctor',
        primaryjoin='Patient.primary_physician_id==Doctor.id',
        backref='main_patients'
    )
    doctors = db.relationship(
        'Doctor',
        secondary=DoctorPatient,
        backref='patients'
    )

    # Unique one-to-one relations
    basic_info_id = db.Column(db.Integer, db.ForeignKey('basic_info.id'))
    basic_info = db.relationship(
        'BasicInfo',
        primaryjoin='Patient.basic_info_id==BasicInfo.id',
        backref='patient'
    )

    legal_family_info_id = db.Column(db.Integer, db.ForeignKey('legal_family_info.id'))
    legal_family_info = db.relationship(
        'LegalFamilyInfo',
        primaryjoin='Patient.legal_family_info_id==LegalFamilyInfo.id',
        backref='patient'
    )
    medical_info_id = db.Column(db.Integer, db.ForeignKey('medical_info.id'))
    medical_info = db.relationship(
        'MedicalInfo',
        primaryjoin='Patient.medical_info_id==MedicalInfo.id',
        backref='patient'
    )
    identifying_info_id = db.Column(db.Integer, db.ForeignKey('identifying_info.id'))
    identifying_info = db.relationship(
        'IdentifyingInfo',
        primaryjoin='Patient.identifying_info_id==IdentifyingInfo.id',
        backref='patient'
    )


class BasicInfo(db.Model):

    __tablename__ = 'basic_info'
    id = db.Column(db.Integer, primary_key=True)
    state_id = db.Column(db.String)
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


class LegalFamilyInfo(db.Model):

    __tablename__ = 'legal_family_info'
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), unique=True, nullable=False)
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


class MedicalInfo(db.Model):

    __tablename__ = 'medical_info'
    id = db.Column(db.Integer, primary_key=True)
    diagnoses = db.Column(db.String)
    allergies = db.Column(db.String)
    alzheimers_dementia = db.Column(db.Boolean)
    down_syndrome = db.Column(db.Boolean)
    vision_problem = db.Column(db.Boolean)


class IdentifyingInfo(db.Model):

    __tablename__ = 'identifying_info'
    id = db.Column(db.Integer, primary_key=True)
    self_protection = db.Column(db.String)
    behavior = db.Column(db.String)
    response_to_search = db.Column(db.String)
    movement_pattern = db.Column(db.String)
    places_frequented = db.Column(db.String)
    travel_method = db.Column(db.String)
    carries_ID = db.Column(db.Boolean)
    surrounding_awareness = db.Column(db.String)
    last_update = db.Column(db.Date)


# TODO: change things like bloodtype, sex, most things to enum. want
# to be able to change all at once.
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


class Program(db.Model):

    __tablename__ = 'program'
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String, nullable=False)


class Staff(db.Model):

    __tablename__ = 'staff'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'))
    position = db.Column(db.String)
    program_id = db.Column(db.Integer, db.ForeignKey('program.id'))
    program = db.relationship(
        "Program",
        primaryjoin='Staff.program_id==Program.id',
        backref="staff"
    )
    address = db.Column(db.String)
    phone = db.Column(db.String(10))


class Doctor(db.Model):

    __tablename__ = 'doctor'
    id = db.Column(db.Integer, primary_key=True)
    name_full = db.Column(db.String)
    specialization = db.Column(db.String)
    address = db.Column(db.String)
    phone = db.Column(db.String(10))
    fax = db.Column(db.String(10))


class HealthInsuranceAndOther(db.Model):

    __tablename__ = 'health_insurance_and_other'
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('Patient.id'))
    source = db.Column(db.String)
    type_of = db.Column(db.String)
    id_number = db.Column(db.String)
    benefits = db.Column(db.String)
    expiration_date = db.Column(db.Date)
    expired = db.Column(db.Boolean)


class SelfPreservation(db.Model):

    __tablename__ = 'self_preservation'
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('Patient.id'))
    assessment = db.Column(db.String)
    cause_of_failure = db.Column(db.String)
    determination_basis = db.Column(db.String)
    date_occurred = db.Column(db.Date)


class LegalCompetency(db.Model):
    __tablename__ = 'legal_competency'
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('Patient.id'))
    status = db.Column(db.String)
    type_of = db.Column(db.String)
    adjudication_date = db.Column(db.Date)
    requested_by = db.Column(db.String)
    date_requested = db.Column(db.Date)


class ServiceProvider(db.Model):
    __tablename__ = 'service_provider'
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('Patient.id'))
    start_date = db.Column(db.Date)
    stop_date = db.Column(db.Date)
    program = db.Column(db.String)
    program_type = db.Column(db.String)
    city_and_state = db.Column(db.String)


class RogersMonitor(db.Model):
    __tablename__ = 'rogers_monitor'
    id = db.Column(db.Integer, primary_key=True)
    next_court_date = db.Column(db.Date)
    last_court_date = db.Column(db.Date)
    guardian_signature_date = db.Column(db.Date)
    appointment_id = db.Column(db.Integer, db.ForeignKey('Appointment.id'))
    medications = db.Column(db.String)


class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    position = db.Column(db.String)
    address = db.Column(db.String)
    phone = db.Column(db.String(10))
    staff = db.relationship("Staff", backref="director")


class BehaviorAssessment(db.Model):
    __tablename__ = 'behavior_assessment'
    id = db.Column(db.Integer, primary_key=True)
    assessment_date = db.Column(db.Date)
    behaviors = db.Column(db.String)
    summary = db.Column(db.String)


class BehaviorSupportPlan(db.Model):
    __tablename__ = 'behavior_support_plan'
    id = db.Column(db.Integer, primary_key=True)
    guardian_signature_date = db.Column(db.Date)
    residential_appointment_id = db.Column(db.Integer, db.ForeignKey('Appointment.id'))
    day_appointment_id = db.Column(db.Integer, db.ForeignKey('Appointment.id'))
    tier = db.Column(db.String)


class IndividualSupportPlan(db.Model):
    __tablename__ = 'individual_support_plan'
    id = db.Column(db.Integer, primary_key=True)
    last_isp_date = db.Column(db.Date, nullable=False)
    comments = db.Column(db.String)


class MedicalTreatmentPlan(db.Model):
    __tablename__ = 'medical_treatment_plan'
    id = db.Column(db.Integer, primary_key=True)
    guardian_signature_date = db.Column(db.Date)
    appointment_id = db.Column(db.Integer, db.ForeignKey('Appointment.id'))
    medications = db.Column(db.String)
    diagnoses = db.Column(db.String)
    symptoms = db.Column(db.String)


class SelfMedication(db.Model):
    __tablename__ = 'self_medication'
    id = db.Column(db.Integer, primary_key=True)
    hrc_approval_date = db.Column(db.Date)
    appointment_id = db.Column(db.Integer, db.ForeignKey('Appointment.id'))

    assessment_score = db.Column(db.Float)
    plan_type = db.Column(db.String)
    physician_signature_date = db.Column(db.Date)
