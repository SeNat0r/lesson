from flask import request, abort, redirect, url_for, render_template

from pony.orm import db_session, ObjectNotFound
from . import app


@app.route('/category/add')
def category_add():
    pass
