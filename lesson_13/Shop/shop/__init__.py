from flask import Flask, render_template
from pony.orm import Database
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_json('../config.json')

CSRFProtect(app)

db = Database()

from . import entities, views

db.bind(app.config['DB_TYPE'], **app.config['DB_CONFIG'])
db.generate_mapping(create_tables=True)
