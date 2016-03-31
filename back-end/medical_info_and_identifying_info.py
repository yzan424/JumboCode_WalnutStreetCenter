class MedicalInfo(db.Model):
    __tablename__ = 'medical_info'
    id = db.Column(db.Integer, primary_key=True)
    diagnoses = db.Column(db.String)
    allergies = db.Column(db.String)
    alzheimers_dementia = db.Column(db.Boolean)
    down_syndrome = db.Column(db.Boolean)
    vision_problem = db.Column(db.Boolean)
#;

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
#;
