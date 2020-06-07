from RandCRM import app
from flask import render_template, request, flash, jsonify
from ..models.user import User

@app.route("/signup", method=["POST"])
def signup():
    """ This api route returns a json object with attribute exists: boolean"""
    email = request.form.get("email", "")
    if email == "":
        return jsonify({"exists": True})

    # If this returns a user, then the email already exists in database
    user = User.query.filter_by(email=email).first()

    # If a user is found, tell the requester.
    return jsonify({"exists": user is None})
