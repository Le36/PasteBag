from app import app
from flask import render_template, request, redirect
from modules.accounts import user_login, user_logout, user_register
from modules.front import most_viewed, create_paste

from modules.paste import paste, raw


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "GET":
        return render_template("index.html", pastes=most_viewed())
    if request.method == "POST":
        return redirect("/" + create_paste())


@app.route("/<paste_id>", methods=["GET"])
def norm_paste(paste_id):
    fetch = paste(paste_id)
    if not fetch:
        return render_template("missing.html")
    return render_template("paste.html", content=fetch["paste"], username=fetch["username"], paste_id=paste_id,
                           views=fetch["views"], title=fetch["title"])


@app.route("/raw/<paste_id>", methods=["GET"])
def raw_paste(paste_id):
    raw_data = raw(paste_id)
    return render_template("missing.html") if not raw_data else raw_data


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        state = user_login()
        return redirect("/") if not state else render_template("login.html", error=state)


@app.route("/logout")
def logout():
    user_logout()
    return redirect("/")


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        state = user_register()
        return render_template("login.html") if not state else render_template("register.html", error=state)
