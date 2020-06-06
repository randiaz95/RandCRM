from RandCRM import app
from flask import redirect, url_for, request, flash, render_template
from werkzeug.security import check_password_hash
from flask_login import login_user
from ..models.user import User

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    user = User.query.filter_by(username=username).first()

    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('main.index'))

    login_user(user, remember=remember)
    return redirect(url_for('main.index'))
