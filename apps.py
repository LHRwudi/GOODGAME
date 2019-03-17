'''尽人事，听天命'''
from flask import Flask
import config
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(config.config_dict['config'])


db = SQLAlchemy(app)

