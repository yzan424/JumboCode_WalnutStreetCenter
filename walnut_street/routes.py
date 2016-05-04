import os

from flask.ext import restless
from jinja2 import Template

from . import models
from . import app


#appointments table NOT ready for production
manager = restless.APIManager(app, flask_sqlalchemy_db=models.db)
default_methods = ('GET', 'PUT', 'POST', 'DELETE')
json_endpoint_models = [
    models.Patient, models.BasicInfo, models.LegalFamilyInfo, models.MedicalInfo, models.IdentifyingInfo, models.SelfPreservation, models.Protocol
]


for model in json_endpoint_models:
    manager.create_api(model, methods=default_methods)


templates_directory = os.path.join(os.path.dirname(__file__), 'templates')


def load_template(filepath):
    with open(filepath) as fileobj:
        return Template(fileobj.read())


# Load all templates in the './templates' filepath and assign them to
# variables in the local scope that correspond to their filenames.
for _, _, filenames in os.walk(templates_directory):
    for filename in filenames:
        template_name = "{}_template".format(filename.split('.')[0])
        locals()[template_name] = load_template(
            os.path.join(templates_directory, filename)
        )


@app.route('/patient/<patient_id>')
def profile(patient_id):
    return profile_template.render(
        profile=models.Patient.query.filter(
            models.Patient.id == patient_id
        ).one()
    )
