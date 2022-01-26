from app import app
from flask import render_template, request, redirect, session, make_response
from db import db
from werkzeug.security import check_password_hash, generate_password_hash


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        import random
        import string
        paste_id = "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=8))
        content = request.form["paste"]
        username = session.get("username", "Anonymous")
        sql = "INSERT INTO pastes (pasteid, paste, username) VALUES (:pasteid, :paste, :username)"
        db.session.execute(sql, {"pasteid": paste_id, "paste": content, "username": username})
        db.session.commit()
        return redirect("/" + paste_id)


@app.route("/<paste_id>", methods=["GET"])
def paste(paste_id):
    sql = "SELECT paste, username FROM pastes WHERE pasteid=:pasteid"
    result = db.session.execute(sql, {"pasteid": paste_id})
    fetched = result.fetchone()
    if not fetched:
        return render_template("missing.html")
    content = fetched["paste"]
    username = fetched["username"]
    return render_template("paste.html", content=content, username=username, paste_id=paste_id)


@app.route("/raw/<paste_id>", methods=["GET"])
def raw_paste(paste_id):
    sql = "SELECT paste FROM pastes WHERE pasteid=:pasteid"
    result = db.session.execute(sql, {"pasteid": paste_id})
    fetched = result.fetchone()
    if not fetched:
        return render_template("missing.html")
    response = make_response(fetched["paste"], 200)
    response.mimetype = "text/plain"
    return response


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        sql = "SELECT id, password FROM users WHERE username=:username"
        result = db.session.execute(sql, {"username": username})
        user = result.fetchone()
        if not user:
            return render_template("login.html", error="Invalid username")
        else:
            hash_value = user.password
            if check_password_hash(hash_value, password):
                session["username"] = username
                return redirect("/")
            else:
                return render_template("login.html", error="Invalid password.")


@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        sql = "SELECT id FROM users WHERE username=:username"
        result = db.session.execute(sql, {"username": username})
        user = result.fetchone()
        if user:
            return render_template("register.html", error="User name is already taken.")
        else:
            hash_value = generate_password_hash(password)
            sql = "INSERT INTO users (username, password, admin) VALUES (:username, :password, false)"
            db.session.execute(sql, {"username": username, "password": hash_value})
            db.session.commit()
            return render_template("login.html")
