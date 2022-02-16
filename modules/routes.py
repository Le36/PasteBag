from app import app
from flask import render_template, request, redirect
from modules.accounts import user_login, user_logout, user_register
from modules.burn import check_burn, burn
from modules.front import most_viewed, create_paste

from modules.paste import paste, raw
from modules.profiles import user_profile


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "GET":
        return render_template("index.html", pastes=most_viewed())
    if request.method == "POST":
        url = create_paste()
        return redirect("/" + url) if not url == "empty" else redirect("/")


@app.route("/<paste_id>", methods=["GET"])
def norm_paste(paste_id):
    fetch = paste(paste_id)
    if not fetch:
        return render_template("missing.html")
    burned = check_burn(paste_id)
    if burned:
        return burned
    return render_template("paste.html", content=fetch["paste"], username=fetch["username"], paste_id=paste_id,
                           views=fetch["views"], title=fetch["title"])


@app.route("/raw/<paste_id>", methods=["GET"])
def raw_paste(paste_id):
    burned = check_burn(paste_id)
    if burned:
        return burned
    raw_data = raw(paste_id, False)
    return render_template("missing.html") if not raw_data else raw_data


@app.route("/burn/<paste_id>", methods=["GET"])
def burn_paste(paste_id):
    burned_paste = burn(paste_id)
    return render_template("missing.html") if not burned_paste else burned_paste


@app.route("/u/<username>", methods=["GET"])
def profile(username):
    user_pastes = user_profile(username)
    return render_template("missing.html") if not user_pastes else render_template("profile.html", pastes=user_pastes)


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
