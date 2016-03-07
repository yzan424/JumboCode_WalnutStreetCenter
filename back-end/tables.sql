/* vim: set foldmarker=CREATE,); foldlevel=0 foldmethod=marker nospell:*/
/* CREATE Note(s): 
        check all NOT NULL fields
        check if all addresses are necessary
        what do we do about sex?
        DATE format YYYY-MM-DD
        height in inches 
        weight in pounds
);*/
CREATE TABLE patients (
    /* basic patient information */
    patient_id INTEGER PRIMARY KEY, /* note: MAY NOT BE INT */
    state_id TEXT,
    name_last TEXT NOT NULL,
    name_first TEXT,
    name_preferred TEXT,
    birthday DATE NOT NULL,
    birthplace TEXT,
    social_security VARCHAR(9),
    citizenship TEXT,
    phone VARCHAR(10),
    phone_on_entry VARCHAR(10),
    group_home INTEGER REFERENCES grouphomes,
    day_service BOOLEAN,
    training_program_or_school_address TEXT,
    training_program_or_school_phone TEXT,
    area_office TEXT,
    record_location TEXT,
    address_current TEXT,
    address_former TEXT,
    sex VARCHAR(10),
    race TEXT,
    blood_type VARCHAR(3),
    religion TEXT,
    marital_status TEXT,
    primary_language TEXT,
    height FLOAT,
    weight FLOAT,
    build TEXT,
    hair TEXT,
    eyes TEXT,
    distinguishing_marks TEXT,
    competency_status TEXT,
    eligibility_date DATE,
    area_meaningful_tie TEXT,
    referral_source TEXT,
    accompanied_by TEXT,
    /* work */
    work_phone VARCHAR(10),
    work_address TEXT,

    /* legal guardian info */
    guardian_name TEXT,
    guardian_phone VARCHAR(10),
    guardian_address TEXT,
    father_name TEXT,
    father_birthday DATE,
    father_birthplace TEXT,
    father_alive BOOLEAN,
    mother_maiden_name TEXT,
    mother_birthday DATE,
    mother_birthplace TEXT,
    mother_alive BOOLEAN,
    parents_marital_status TEXT,

    /* family info */
    family_phone VARCHAR(10),
    family_address TEXT,


    /* medical info */
    physician_id INTEGER REFERENCES physicians, /* TODO: Remove in ORM, replace w/ relation */
    diagnoses TEXT,
    allergies TEXT,
    alzheimers_dementia BOOLEAN,
    down_syndrome BOOLEAN,
    vision_problem BOOLEAN,

    /* identifying info */
    self_protection TEXT,
    behavior TEXT,
    response_to_search TEXT,
    movement_pattern TEXT,
    places_frequented TEXT,
    travel_method TEXT,
    carries_ID BOOLEAN,
    surrounding_awareness TEXT,

    last_update DATE NOT NULL
);
/* DOES NOT COVER ALL providers, only primary */
/* TODO: Have separate table containing {patient_id, doctor_id} */
CREATE TABLE doctor_list (
);
CREATE TABLE doctors (
    doctor_id SERIAL PRIMARY KEY,
    full_name  VARCHAR(50),
    specialization VARCHAR(30),
    address VARCHAR(50),
    phone VARCHAR(20),
    fax VARCHAR(20)
);
CREATE TABLE programs (
       program_id SERIAL PRIMARY KEY,
       address TEXT NOT NULL
);
CREATE TABLE contacts (
    contact_id SERIAL PRIMARY KEY,
    name TEXT,
    patient_id INTEGER REFERENCES patients,
    relation TEXT,
    address TEXT,
    phone VARCHAR(10),
    date_added DATE,
    date_removed DATE,
    removal_reason TEXT,
    primary_contact BOOLEAN
);
CREATE TABLE staff (
    staff_id SERIAL PRIMARY KEY,
    name TEXT,
    email_address TEXT,
    director_id REFERENCES directors,
    position TEXT,
    program_id INTEGER REFERENCES programs,
    address TEXT,
    phone VARCHAR(10)
);
CREATE TABLE directors (
    director_id SERIAL PRIMARY KEY,
    name TEXT,
    email_address TEXT,
    position TEXT,
    address TEXT,
    phone VARCHAR(10)
);

CREATE TABLE health_insurance_and_other (
    health_insurance_and_other_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients,
    source TEXT,
    type_of TEXT,
    id_number TEXT,
    benefits TEXT,
    expiration_date DATE,
    expired BOOLEAN
);
/* Note: In preservation table, Date is monthly*/
CREATE TABLE self_preservation (
    self_preservation_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients,
    assessment TEXT,
    cause_of_failure TEXT,
    determination_basis TEXT,
    date_occurred DATE
);
CREATE TABLE legal_competency (
    legal_competency_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients,
    status TEXT,
    type_of TEXT,
    adjudication_date DATE,
    requested_by TEXT,
    date_requested DATE
);
CREATE TABLE service_providers (
    service_providers_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients,
    start_date DATE,
    stop_date DATE,
    program TEXT,
    program_type TEXT,
    city_and_state TEXT
);
/* Note: HRC Approval dates ALL expire after one year
         ALL Guardian signatures expire after one year
         ALL Training dates expire after one year     */
CREATE TABLE  appointments (
    appointment_id SERIAL PRIMARY KEY,
    appointment_type TEXT NOT NULL,
    patient_id INTEGER REFERENCES patients,
    last_appointment DATE,
    frequency INTEGER, /*  Note: stored in months*/
    next_appointment TIMESTAMP,
    new_medication BOOLEAN,
    doctor_id INTEGER REFERENCES doctors,
    staff_id INTEGER REFERENCES staff
);
CREATE TABLE protocols (
    protocol_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients,
    name TEXT,
    description TEXT,
    appointment_id INTEGER REFERENCES appointments,
    guardian_signature_date DATE,
    physician_signature_date DATE
);
CREATE TABLE self_medication ( /* TODO: Make subclass of patients */
    patient_id INTEGER REFERENCES patients NOT NULL UNIQUE,
    hrc_approval_date DATE,
    appointment_id INTEGER REFERENCES appointments,
    assessment_score FLOAT,
    plan_type TEXT,
    physician_signature_date DATE
);
CREATE TABLE supportive_protective_devices (
    supportive_protective_devices_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients,
    device_type TEXT,
    hrc_approval_date DATE, /* Expiration date one year later */
    hrc_submission_date DATE, /* get rid of this??? */
    physician_signature BOOLEAN,
    nurse_signature BOOLEAN
);
CREATE TABLE individual_support_plans ( /* TODO: Make subclass of patients */
    individual_support_plan_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients NOT NULL,
    last_isp_date DATE NOT NULL, /* Note: Several dates derive from this */
    comments TEXT
);
CREATE TABLE tracking (
    tracking_id SERIAL PRIMARY KEY,
    tracking_name TEXT, /*TODO: Find better name*/
    description TEXT,
    most_recent DATE,
    next_due INTEGER /* In months */
);
CREATE TABLE medical_treatment_plan ( /* TODO: Make subclass of patients */
    medical_treatment_plan_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients,
    guardian_signature_date DATE,
    appointment_id INTEGER REFERENCES appointments,
    medications TEXT,
    diagnoses TEXT,
    symptoms TEXT
);
CREATE TABLE  behavior_assessments ( /* TODO: Make subclass of patients */
    patient_id INTEGER REFERENCES patients NOT NULL UNIQUE,
    assessment_date DATE,
    behaviors TEXT,
    summary TEXT
);
CREATE TABLE restrictive_practices (
    restrictive_practices_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients,
    practice_type TEXT,
    hrc_approval_date DATE,
    hrc_submission_date DATE,
    description TEXT
);
CREATE TABLE behavior_support_plans ( /* TODO: Make subclass of patients */
    patient_id INTEGER REFERENCES patients,
    guardian_signature_date DATE,
    /* TODO: Make sure we can reference these like this*/
    residential_appointment_id INTEGER REFERENCES appointments,
    day_appointment_id INTEGER REFERENCES appointments,
    tier TEXT
);
CREATE TABLE rogers_monitor ( /* TODO: Make subclass of patients */
    patient_id INTEGER REFERENCES patients NOT NULL UNIQUE,
    next_court_date DATE,
    last_court_date DATE,
    guardian_signature_date DATE,
    appointment_id INTEGER REFERENCES appointments,
    medications TEXT
);
