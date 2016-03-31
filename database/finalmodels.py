# vim: set foldmarker=class,; foldlevel=0 foldmethod=marker nospell:
# class preamble
from sqlalchemy import Column, String, Integer, ForeignKey                                 
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

patient_doctor = Table('patient_doctor', Base.metadata,
    Column('patient_id', Integer, ForeignKey('patient.id')),
    Column('doctor_id', Integer, ForeignKey('doctor.id'))
)
#;
class patient(Base):
    __tablename__ = 'patient'
    id = Column(Integer, primary_key=True)

    program_id = Column(Integer, ForeignKey('program.id'), unique=True)
    program = relationship("program", back_populates="patients")
    doctors = relationship("doctor",
                            secondary=patient_doctor,
                            back_populates="patients")
    primary_physician = Column(Integer, ForeignKey('doctor.id'), unique=True)

    """ Many-one relations """
    contacts = relationship("contact", back_populates="patient")
    health_insurance_and_other = relationship("health_insurance_and_other",
                                              back_populates = "patient")
    self_preservation = relationship("self_preservation", back_populates="patient")
    legal_competency = relationship("legal_competency", back_populates="patient")
    service_providers = relationship("service_provider", 
                                     back_populates = "patient")
    supportive_protective_devices = relationship("supportive_protective_device",
                                                 back_populates = "patient")
    tracking = relationship("tracking", back_populates = "patient")
    restrictive_practices = relationship("restrictive_practice", 
                                         back_populates="patient")

    """ Unique one-to-one relations """
    basic_info = relationship("basic_info", 
            uselist=False, back_populates="patient")
    legal_guardian_and_family_info = relationship("legal_guardian_and_family_info",
            uselist=False, back_populates="patient")
    medical_info = relationship("medical_info", 
            uselist=False, back_populates="patient")
    identifying_info = relationship("identifying_info", 
            uselist=False, back_populates="patient")
    self_medication = relationship("self_medication", 
            uselist=False, back_populates="patient")
    individual_support_plan = relationship("individual_support_plan", 
            uselist=False, back_populates="patient")
    medical_treatment_plan = relationship("medical_treatment_plan", 
            uselist=False, back_populates="patient")
    behavior_assessment = relationship("behavior_assessment", 
            uselist=False, back_populates="patient")
    behavior_support_plan = relationship("behavior_support_plan", 
            uselist=False, back_populates="patient")
    rogers_monitor = relationship("rogers_monitor", 
            uselist=False, back_populates="patient")

    """ Non-unique one-to-one relations """
#;
class basic_info(Base):
    __tablename__ = 'basic_info'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patient.id'), unique=True, nullable=False)
    patient = relationship("patient", back_populates="basic_info")
    state_id = Column(String)
    name_first = Column(String)
    name_last = Column(String)
    name_preferred = Column(String)
    birthday = Column(Date)
    birthplace = Column(String)
    social_security = Column(String(9))
    citizenship = Column(String)
    phone = Column(String(10))
    phone_on_entry = Column(String(10))
    day_service = Column(Boolean)
    training_program_or_school_address = Column(String)
    training_program_or_school_phone = Column(String(10))
    area_office = Column(String)
    record_location = Column(String)
    address_current = Column(String)
    address_former = Column(String)
    sex = Column(String)
    race = Column(String)
    blood_type = Column(String)
    religion = Column(String)
    marital_status = Column(String)
    primary_language = Column(String)
    height = Column(Float)
    weight = Column(Float)
    build = Column(String)
    hair = Column(String)
    eyes = Column(String)
    distinguishing_marks = Column(String)
    competency_status = Column(String)
    eligibility_date = Column(Date)
    area_meaningful_tie = Column(String)
    referral_source = Column(String)
    accompanied_by = Column(String)
    work_phone = Column(String(10))
    work_address = Column(String)
#;
class legal_guardian_and_family_info(Base):
    __tablename__ = 'legal_guardian_and_family_info'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patient.id'), unique=True, nullable=False)
    patient = relationship("patient",
            back_populates="legal_guardian_and_family_info")
    guardian_name = Column(String)
    guardian_phone = Column(String)
    guardian_address = Column(String)
    father_name = Column(String)
    father_birthday = Column(Date)
    father_birthplace = Column(String)
    father_alive = Column(Boolean)
    mother_maiden_name = Column(String)
    mother_birthday = Column(Date)
    mother_birthplace = Column(String)
    mother_alive = Column(Boolean)
    parents_marital_status = Column(String)
    family_phone = Column(String(10))
    family_address = Column(String)
#;
# TODO: Add many-many relation between medical_info and doctors
class medical_info(Base):
    __tablename__ = 'medical_info'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patient.id'), unique=True, nullable=False)
    patient = relationship("patient", back_populates="medical_info")
    diagnoses = Column(String)
    allergies = Column(String)
    alzheimers_dementia = Column(Boolean)
    down_syndrome = Column(Boolean)
    vision_problem = Column(Boolean)
#;
class identifying_info(Base):
    __tablename__ = 'identifying_info'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patient.id'), unique=True, nullable=False)
    patient = relationship("patient", back_populates="identifying_info")

    self_protection = Column(String)
    behavior = Column(String)
    response_to_search = Column(String)
    movement_pattern = Column(String)
    places_frequented = Column(String)
    travel_method = Column(String)
    carries_ID = Column(Boolean)
    surrounding_awareness = Column(String)
    last_update = Column(Date)
#;
class self_medication(Base):
    __tablename__ = 'self_medication'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patient.id'), unique=True, nullable=False)
    patient = relationship("patient", back_populates="self_medication")
    hrc_approval_date = Column(Date)
    appointment_id = Column(Integer, ForeignKey('appointment.id'))

    assessment_score = Column(Float)
    plan_type = Column(String)
    physician_signature_date = Column(Date)
#;
class individual_support_plan(Base):
    __tablename__ = 'individual_support_plan'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patient.id'), unique=True, nullable=False)
    patient = relationship("patient", back_populates="individual_support_plan")
    last_isp_date = Column(Date, nullable=False)
    comments = Column(String)
#;
class medical_treatment_plan(Base):
    __tablename__ = 'medical_treatment_plan'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patient.id'), unique=True, nullable=False)
    patient = relationship("patient", back_populates="medical_treatment_plan")
    guardian_signature_date = Column(Date)
    appointment_id = Column(Integer, ForeignKey('appointment.id'))
    medications = Column(String)
    diagnoses = Column(String)
    symptoms = Column(String)
#;
class behavior_assessment(Base):
    __tablename__ = 'behavior_assessment'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patient.id'), unique=True, nullable=False)
    patient = relationship("patient", back_populates="behavior_assessment")
    assessment_date = Column(Date)
    behaviors = Column(String)
    summary = Column(String)
#;
class behavior_support_plan(Base):
    __tablename__ = 'behavior_support_plan'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patient.id'), unique=True, nullable=False)
    patient = relationship("patient", back_populates="behavior_support_plan")
    guardian_signature_date = Column(Date)
    residential_appointment_id = Column(Integer, ForeignKey('appointment.id'))
    day_appointment_id = Column(Integer, ForeignKey('appointment.id'))
    tier = Column(String)
#;
class rogers_monitor(Base):
    __tablename__ = 'rogers_monitor'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patient.id'), unique=True, nullable=False)
    patient = relationship("patient", back_populates="rogers_monitor")
    next_court_date = Column(Date)
    last_court_date = Column(Date)
    guardian_signature_date = Column(Date)
    appointment_id = Column(Integer, ForeignKey('appointment.id'))
    medications = Column(String)
#;

class doctor(Base):
    __tablename__ = 'doctor'
    id = Column(Integer, primary_key=True)
    name_full = Column(String)
    specialization = Column(String)
    address = Column(String)
    phone = Column(String(10))
    fax = Column(String(10))
    patients = relationship("patient",
                            secondary=patient_doctor,
                            back_populates="doctors")
#;
class contact(Base):
    __tablename__ = 'contact'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    patient_id = Column(Integer, ForeignKey('patient.id'))
    patient = relationship("patient", back_populates="contacts")
    relation = Column(String)
    address = Column(String)
    date_added = Column(Date)
    date_removed = Column(Date)
    removal_reason = Column(String)
    primary_contact = Column(Boolean)
#;

class director(Base):
    __tablename__ = 'director'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    position = Column(String)
    address = Column(String)
    phone = Column(String(10))
    staff = relationship("staff", back_populates="director")
#;
class program(Base):
    __tablename__ = 'program'
    id = Column(Integer, primary_key=True)
    address = Column(String, nullable=False)
    patients = relationship("patient", back_populates="program")
    staff = relationship("staff", back_populates="program")
#;
class staff(Base):
    __tablename__ = 'staff'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    director_id = Column(Integer, ForeignKey('director.id'))
    director = relationship("director", back_populates="staff")
    position = Column(String)
    program_id = Column(Integer, ForeignKey('program.id'))
    program = relationship("program", back_populates="staff")
    address = Column(String)
    phone = Column(String(10))
#;

class health_insurance_and_other(Base):
    __tablename__ = 'health_insurance_and_other'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patient.id'))
    patient = relationship("patient", back_populates="health_insurance_and_other")
    source = Column(String)
    type_of = Column(String)
    id_number = Column(String)
    benefits = Column(String)
    expiration_date = Column(Date)
    expired = Column(Boolean)
#;
class self_preservation(Base):
    __tablename__ = 'self_preservation'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patient.id'))
    patient = relationship("patient", back_populates="self_preservation")
    assessment = Column(String)
    cause_of_failure = Column(String)
    determination_basis = Column(String)
    date_occurred = Column(date)
#;
class legal_competency(Base):
    __tablename__ = 'legal_competency'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patient.id'))
    patient = relationship("patient", back_populates="legal_competency")
    status = Column(String)
    type_of = Column(String)
    adjudication_date = Column(Date)
    requested_by = Column(String)
    date_requested = Column(date)
#;
class service_provider(Base):
    __tablename__ = 'service_provider'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patient.id'))
    patient = relationship("patient", back_populates="service_providers")
    start_date = Column(Date)
    stop_date = Column(Date)
    program = Column(String)
    program_type = Column(String)
    city_and_state = Column(String)
#;
""" NOTE: class 
         HRC Approval dates ALL expire after one year
         ALL Guardian signatures expire after one year
         ALL Training dates expire after one year    ;"""
#TODO: Appointment relationships
class appointment(Base):
    __tablename__ = 'appointment'
    id = Column(Integer, primary_key=True)
    appointment_type = Column(String, nullable=False)
    address = Column(String)
    patient_id = Column(Integer, ForeignKey('patient.id'))
    last_appointment = Column(Date)
    frequency = Column(Integer) # NOTE: in months
    next_appointment = Column(DateTime)
    new_medication = Column(Boolean)
    doctor_id = Column(Integer, ForeignKey('doctor.id'))
    staff_id = Column(Integer, ForeignKey('staff.id'))
#;
class protocol(Base):
    __tablename__ = 'protocol'
    id = Column(Integer, primary_key=True)
    # NOTE: patient.id can be derived from appointment
    appointment_id = Column(Integer, ForeignKey('appointment.id'))
    name = Column(String)
    description = Column(String)
    guardian_signature_date = Column(Date)
    physician_signature_date = Column(Date)
#;
class supportive_protective_device(Base):
    __tablename__ = 'supportive_protective_device'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patient.id'))
    patient = relationship("patient",
                            back_populates="supportive_protective_devices")
    device_type = Column(String)
    hrc_approval_date = Column(Date)
    hrc_submission_date = Column(Date)
    physician_signature_date = Column(Date)
    physician_signature = Column(Boolean)
    nurse_signature = Column(Boolean)
#;
class tracking(Base):
    __tablename__ = 'tracking'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patient.id'))
    patient = relationship("patient", back_populates="tracking")
    name = Column(String)
    description = Column(String)
    most_recent = Column(Date)
    next_due = Column(Integer) # in months
#;
class restrictive_practice(Base):
    __tablename__ = 'restrictive_practice'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patient.id'))
    patient = relationship("patient", back_populates="restrictive_practices")
    practice_type = Column(String)
    hrc_approval_date = Column(Date)
    hrc_submission_date = Column(Date)
    description = Column(String)
#;
