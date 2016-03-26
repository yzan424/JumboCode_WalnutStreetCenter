from flask.ext import restless
from . import models
from . import app


manager = restless.APIManager(app, flask_sqlalchemy_db=models.db)

manager.create_api(models.Patient, methods=['GET', 'PUT', 'POST', 'DELETE'])
manager.create_api(models.BasicInfo, methods=['GET', 'PUT', 'POST', 'DELETE'])
