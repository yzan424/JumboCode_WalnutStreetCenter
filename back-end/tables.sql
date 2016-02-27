/* vim: set foldmarker=CREATE,); foldlevel=0 foldmethod=marker nospell:*/
/*
    Note(s): 
        check all NOT NULL fields
        check if all addresses are necessary
        what do we do about sex?
        DATE format YYYY-MM-DD
        height in inches 
        weight in pounds
*/
CREATE TABLE patients (
    /* basic patient information */
    patient_id INTEGER PRIMARY KEY, /* note: MAY NOT BE INT */
    state_id VARCHAR(20),
    name_last VARCHAR(50) NOT NULL,
    name_first VARCHAR(50),
    name_preferred VARCHAR(50),
    birthday DATE NOT NULL,
    birthplace VARCHAR(50),
    social_security VARCHAR(9),
    citizenship VARCHAR(20),
    phone VARCHAR(10),
    phone_on_entry VARCHAR(10),
    group_home INTEGER REFERENCES grouphomes,
    day_service BOOLEAN,
    training_program_or_school_address VARCHAR(50),
    training_program_or_school_phone VARCHAR(50),
    area_office INTEGER,
    record_location TEXT,
    address_current TEXT,
    address_former TEXT,
    sex VARCHAR(10),
    race VARCHAR(20),
    blood_type VARCHAR(5),
    religion VARCHAR(20),
    marital_status VARCHAR(20),
    primary_language VARCHAR(50),
    height FLOAT NOT NULL,
    weight FLOAT NOT NULL,
    build VARCHAR(20),
    hair VARCHAR(20),
    eyes VARCHAR(20),
    distinguishing_marks VARCHAR(100),
    competency_status VARCHAR(100),
    eligibility_date DATE,
    area_meaningful_tie VARCHAR(50),
    referral_source VARCHAR(50),
    accompanied_by VARCHAR(50),
    /* TODO: add check boxes to patient info*/

    /* legal guardian info */
    guardian_name VARCHAR(50),
    guardian_phone VARCHAR(20),
    guardian_address VARCHAR(50),
    father_name VARCHAR(50),
    father_birthday DATE,
    father_birthplace VARCHAR(50),
    father_alive BOOLEAN,
    mother_maiden_name VARCHAR(50),
    mother_birthday DATE,
    mother_birthplace VARCHAR(50),
    mother_alive BOOLEAN,
    parents_marital_status VARCHAR(20),

    /* family info */
    family_phone VARCHAR(50),
    family_address VARCHAR(50),

    /* work */
    work_phone VARCHAR(20),
    work_address VARCHAR(50),

    /* medical info */
    physician_id INTEGER REFERENCES physicians,
    diagnoses VARCHAR(800), 
    allergies VARCHAR(500), 
    alzheimers_dementia BOOLEAN,
    down_syndrome BOOLEAN,
    vision_problem BOOLEAN,

    /* identifying info */
    self_protection VARCHAR(200),
    behavior VARCHAR(200),
    response_to_search VARCHAR(200),
    movement_pattern VARCHAR(200),
    places_frequented VARCHAR(200),
    travel_method VARCHAR(200),
    carries_ID BOOLEAN,
    surrounding_awareness VARCHAR(200),

    /* table references */
    /*TODO Remove these*/
    self_medication_id INTEGER REFERENCES self_medication,
    individual_support_plan_id INTEGER REFERENCES individual_support_plans,
    medical_treatment_plan_id INTEGER REFERENCES medical_treatment_plans,

    last_update DATE NOT NULL
);
/* DOES NOT COVER ALL providers, only primary */
/* TODO: Have separate table containing {patient_id, doctor_id} */
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
       address VARCHAR() NOT NULL,
       manager_id INTEGER REFERENCES managers NOT NULL
);
CREATE TABLE contacts (
    name
    patient_id
    relation
    address
    phone
    date_added
    date_removed
    removal_reason
    primary_contact BOOLEAN
);
CREATE TABLE staff (
    name
    group_home 
    email_address TEXT,
    director_id
    position
    address
    phone
);
/* TODO: Group Home table */
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
    appointment_type
    patient_id INTEGER REFERENCES patients,
    last_appointment DATE,
    frequency INTEGER, /*  Note: stored in months*/
    next_appointment TIMESTAMP,
    new_medication BOOLEAN,
    contact
);
CREATE TABLE protocols (
    protocol_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients,
    name TEXT,
    description TEXT,
    last_training_date DATE,
    next_training_date TIMESTAMP,
    guardian_signature_date DATE,
    physician_signature_date DATE
);
CREATE TABLE self_medication (
    self_medication_id SERIAL PRIMARY KEY,
    hrc_approval_date DATE,
    last_training_date DATE,
    next_training_date TIMESTAMP,
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
CREATE TABLE individual_support_plans (
    individual_support_plan_id SERIAL PRIMARY KEY,
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
CREATE TABLE medical_treatment_plan (
    medical_treatment_plan_id SERIAL PRIMARY KEY,
    guardian_signature_date DATE,
    last_training_date DATE,
    next_training_date TIMESTAMP,
    medications TEXT,
    diagnoses TEXT,
    symptoms TEXT
);
/* TODO: Are patient_ids primary keys? */
CREATE TABLE  behavior_assessments (
    behavior_assessment_id SERIAL PRIMARY KEY,
    patient_id UNIQUE INTEGER REFERENCES patients,
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
CREATE TABLE behavior_support_plans (
    patient_id INTEGER REFERENCES patients,
    guardian_signature_date DATE,

    last_residential_training_date DATE,
    next_residential_training_date TIMESTAMP,
    last_day_training_date DATE,
    next_day_training_date TIMESTAMP,
    tier TEXT
);
CREATE TABLE rogers_monitor (
    patient_id UNIQUE INTEGER REFERENCES patients,
    next_court_date DATE,
    last_court_date DATE,
    guardian_signature_date DATE,
    last_training_date DATE,
    next_training_date TIMESTAMP,
    medications TEXT
);
