from flask.ext import restless
from . import models
from . import app


manager = restless.APIManager(app, flask_sqlalchemy_db=models.db)

manager.create_api(models.Patient, methods=['GET', 'PUT', 'POST', 'DELETE'])
manager.create_api(models.BasicInfo, methods=['GET', 'PUT', 'POST', 'DELETE'])
manager.create_api(models.LegalFamilyInfo, methods=['GET', 'PUT', 'POST', 'DELETE'])
manager.create_api(models.MedicalInfo, methods=['GET', 'PUT', 'POST', 'DELETE'])
manager.create_api(models.IdentifyingInfo, methods=['GET', 'PUT', 'POST', 'DELETE'])
manager.create_api(models.Contact, methods=['GET', 'PUT', 'POST', 'DELETE'])
manager.create_api(models.Program, methods=['GET', 'PUT', 'POST', 'DELETE'])
manager.create_api(models.Staff, methods=['GET', 'PUT', 'POST', 'DELETE'])
manager.create_api(models.Doctor, methods=['GET', 'PUT', 'POST', 'DELETE'])
