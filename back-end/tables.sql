/*
    Note(s): 
        check patient_id
        check all NOT NULL fields
        check if all addresses are necessary
        what do we do about sex?
        DATE format YYYY-MM-DD
        height in inches 
        weight in pounds
        medications?
*/
CREATE TABLE patients (
    /* basic patient information */
    patient_id INTEGER PRIMARY KEY, /* note: MAY NOT BE INT */
    state_id VARCHAR(50),
    name_last VARCHAR(50) NOT NULL,
    name_first VARCHAR(50),
    name_preferred VARCHAR(50),
    birthday DATE NOT NULL,
    photo VARBINARY(MAX), /* TODO: ensure photo type in interface i.e. jpeg*/
    phone VARCHAR(20),
    program INTEGER REFERENCES programs,
    area INTEGER,
    address_current VARCHAR(50) NOT NULL,
    address_on_entry VARCHAR(50) NOT NULL,
    sex VARCHAR(10) NOT NULL,
    race VARCHAR(20),
    primary_language VARCHAR(50),
    height FLOAT NOT NULL,
    weight FLOAT NOT NULL,
    build VARCHAR(20),
    hair VARCHAR(20),
    eyes VARCHAR(20),
    distinguishing_marks VARCHAR(100),
    competency_status VARCHAR(100),
    /* TODO: add check boxes to patient info*/

    /* legal guardian info */
    guardian_name VARCHAR(50),
    guardian_phone VARCHAR(20),
    guardian_address VARCHAR(50),

    /* family info */
    family_phone VARCHAR(50),
    family_address VARCHAR(50),

    /* work */
    work_phone VARCHAR(20),
    work_address VARCHAR(50),

    /* medical info */
    physician_id INTEGER REFERENCES physicians,
    diagnoses VARCHAR(200), /* Note: Leave as a text field*/
    allergies VARCHAR(200), /* table? */
    /*TODO: MEDICATIONS reference a table? */

    /* identifying info */
    self_protection VARCHAR(50),
    behavior VARCHAR(500),
    response_to_search VARCHAR(500),
    movement_pattern VARCHAR(200),
    places_frequented VARCHAR(200),
    travel_method VARCHAR(50),
    carries_ID BOOLEAN,
    surrounding_awareness VARCHAR(50),
    probable_dress VARCHAR(200),
    location_last_seen VARCHAR(100),
    time_last_seen TIMESTAMP, /* note: extract date from this */

    last_update DATE NOT NULL
);

/* DOES NOT COVER ALL providers, only primary */
/*
    Note: Have separate table containing {patient_id, doctor_id}
*/
CREATE TABLE doctors (
    doctor_id SERIAL PRIMARY KEY,
    full_name  VARCHAR(50),
    specialization VARCHAR(30),
    address VARCHAR(50),
    phone VARCHAR(20),
    fax VARCHAR(20)
);

/* separate form */
CREATE TABLE  appointments (
       
);

CREATE TABLE programs (
       program_id SERIAL PRIMARY KEY,
       address VARCHAR() NOT NULL,
       manager_id INTEGER REFERENCES managers NOT NULL
);
    
CREATE TABLE diagnoses (

);

/* TODO: We probably do not need this table */
CREATE TABLE medications (
       patient_id INTEGER REFERENCES patients NOT NULL,
       med_name VARCHAR(50) NOT NULL,
       dose VARCHAR(20),
       frequency VARCHAR(50),
       route VARCHAR(30),
       purpose VARCHAR(30),
       provider VARCHAR(30)
);           

CREATE TABLE contacts
/* ADDED field = date added???*/
    Contact person
    Contact person phone
    Contact person address

/* TODO: In preservation table, Date is monthly*/

/* TODO: Do NOT make each type of exam their own table, leave as a blank varchar
 * field
 */

/* 
 * TODO: Make table of walnut street staff with same fields as contacts table
 * plus group home and position and email
 */

 /*TODO: Include blood type */

/* Note: HRC Approval dates ALL expire after one year
         ALL Guardian signatures expire after one year
         ALL Training dates expire after one year
*/

/*
Linked fields:
Training program/school ID
Physician ID
*/
