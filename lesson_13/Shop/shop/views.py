from flask import request, abort, redirect, url_for, render_template
from pony.orm import db_session, ObjectNotFound
from . import app
from .forms import CategoryForm
from .entities import Category


@app.route('/category/add', methods=['GET', 'POST'])
def category_add():
    form = CategoryForm(request.form)

    if form.validate_on_submit():
        with db_session:
            category = Category(title=form.title.data)
        return redirect(url_for('category_edit', category_id=category.id))

    return render_template('category/add.html', form=form)


@app.route('/category/edit/<int:category_id>', methods=['GET', 'POST'])
def category_edit(category_id):
    pass
