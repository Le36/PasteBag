from flask import request, session
from werkzeug.security import check_password_hash, generate_password_hash

from utils.db import db


def user_login():
    username = request.form["username"]
    if len(username) == 0:
        return "Username cannot be empty."
    password = request.form["password"]
    if len(password) == 0:
        return "Password cannot be empty."
    sql = "SELECT password, admin FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    user = result.fetchone()
    if not user:
        return "Invalid username"
    else:
        hash_value = user.password
        if check_password_hash(hash_value, password):
            session["username"] = username
            if user.admin:
                session["admin"] = True
            else:
                session["admin"] = False
            return
        else:
            return "Invalid password."


def user_logout():
    del session["username"]
    del session["admin"]


def user_register():
    username = request.form["username"]
    if len(username) == 0:
        return "Username cannot be empty."
    password = request.form["password"]
    if len(password) == 0:
        return "Password cannot be empty."
    sql = "SELECT id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    user = result.fetchone()
    if user:
        return "Username is already taken."
    else:
        hash_value = generate_password_hash(password)
        sql = "INSERT INTO users (username, password, admin) VALUES (:username, :password, false)"
        db.session.execute(sql, {"username": username, "password": hash_value})
        db.session.commit()
        return
