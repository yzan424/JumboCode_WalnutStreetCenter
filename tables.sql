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
    patient_id INTEGER PRIMARY KEY, /* MAY NOT BE INT */
    name_last VARCHAR(50) NOT NULL,
    name_first VARCHAR(50),
    /*TODO: Make grouphome id that references grouphome table*/
    name_preferred VARCHAR(50),
    photo VARBINARY(MAX), /* TODO: ensure photo type in interface i.e. jpeg*/
    phone VARCHAR(20),
    address_current VARCHAR(50) NOT NULL,
    address_former VARCHAR(50),
    address_on_entry VARCHAR(50) NOT NULL,
    sex VARCHAR(10) NOT NULL,
    race VARCHAR(20),
    language VARCHAR(50),
    birthday DATE NOT NULL,
    height FLOAT NOT NULL,
    weight FLOAT NOT NULL,
    build VARCHAR(20),
    hair VARCHAR(20),
    eyes VARCHAR(20),
    distinguishing_marks VARCHAR(100),
    competency_status VARCHAR(100),

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
    diagnoses VARCHAR(200),
    allergies VARCHAR(200),
    /*TODO: MEDICATIONS reference a table? */

    /* identifying info */
    self_protection VARCHAR(50),
    behavior VARCHAR(500),
    response_to_search VARCHAR(500),
    movement_pattern VARCHAR(200),
    places_frequented VARCHAR(200),
    /*TODO: relevant capabilities, limitations, and preferences????*/
    probable_dress VARCHAR(200),
    last_known_location VARCHAR(100),
    time_last_known_location TIMESTAMP, /* note: extract date from this */

    last_update DATE NOT NULL
);

CREATE TABLE physicians (
    physician_id SERIAL PRIMARY KEY,
    name_first VARCHAR(50),
    name_last VARCHAR(50),
    address VARCHAR(50),
    phone VARCHAR(20)
);


/* extract this info from primary contact of contacts table
    Contact person
    Contact person phone
    Contact person address
*/

/*
Linked fields:
Training program/school ID
Physician ID
*/
