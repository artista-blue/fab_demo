"""__init__.py"""
import logging

from flask import Flask
from flask_appbuilder import AppBuilder, SQLA

# Logging configuration
logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

# Creating and configuring flask app
app = Flask(__name__)
app.config.from_object("config")
db = SQLA(app)
appbuilder = AppBuilder(app, db.session)

from . import views # pylint: disable=C0413
