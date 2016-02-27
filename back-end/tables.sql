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
CREATE TABLE health_insurance_and_other (
    source TEXT,
    type_of TEXT,
    id_number TEXT,
    benefits TEXT,
    expiration_date DATE,
    expired BOOLEAN
);
/* Note: In preservation table, Date is monthly*/
CREATE TABLE self_preservation (
    assessment TEXT,
    cause_of_failure TEXT,
    determination_basis TEXT,
    date_occurred DATE
);
CREATE TABLE legal_competency (
    status TEXT,
    type_of TEXT,
    adjudication_date DATE,
    requested_by TEXT,
    date_requested DATE
);
CREATE TABLE service_providers (
    start_date DATE,
    stop_date DATE,
    program TEXT,
    program_type TEXT,
    city_and_state TEXT
);
/* Note: HRC Approval dates ALL expire after one year
         ALL Guardian signatures expire after one year
         ALL Training dates expire after one year     */

/* separate form */
CREATE TABLE  appointments (
    appointment_type
    last_appointment DATE,
    frequency INTEGER, /*  Note: stored in months*/
    next_appointment TIMESTAMP,
    new_medication BOOLEAN,
    contact
);

/*
Linked fields:
Training program/school ID
Physician ID
*/
