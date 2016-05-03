from __future__ import absolute_import
import os

from flask import Flask, url_for
import flask.ext.whooshalchemy

application_directory = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://localhost/walnut_dev'
app.config['WHOOSH_BASE'] = '../Whoosh-2.7.4'

app.debug = True
