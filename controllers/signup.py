from RandCRM import app
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user
from werkzeug.security import generate_password_hash
from ..models.user import User
from .. import db


@app.route("/signup", method=["POST"])
def signup():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')

    # create new user with the form data. Hash the password so plaintext version isn't saved.
    new_user = User(email=email, username=username,
                    password=generate_password_hash(password, method='sha256'),
                    active=False)

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    login_user(new_user)
    return render_template('index.html', confirm=True, uid=generate_password_hash(new_user.id, method='sha256'))
