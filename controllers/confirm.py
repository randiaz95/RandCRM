from RandCRM import app
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user
from werkzeug.security import generate_password_hash
from ..models.user import User
from .. import db


@app.route("/confirm", method=["POST"])
def confirm():
    uid = request.form.get('uid')
    code = request.form.get('code')

    user = User.query.filter_by(id=uid).first()

    if user:
        flash("This email is already being used.")
        return render_template('index.html', login_state='signup')

    user.active = True

    db.session.commit()

    login_user(new_user)
    return render_template('index.html', confirm=True)
