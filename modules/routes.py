from app import app
from flask import render_template, request, redirect, session
from modules.accounts import user_login, user_logout, user_register
from modules.burn import check_burn, burn
from modules.contact import contact
from modules.front import most_viewed, create_paste

from modules.paste import paste, raw, confirm
from modules.profiles import public_pastes, about, picture, post_picture


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "GET":
        return render_template("index.html", pastes=most_viewed())
    if request.method == "POST":
        url = create_paste()
        return redirect("/" + url) if not url == "empty" else redirect("/")


@app.route("/<paste_id>", methods=["POST", "GET"])
def norm_paste(paste_id):
    if request.method == "GET":
        fetch = paste(paste_id)
        if not fetch:
            return render_template("missing.html")
        burned = check_burn(paste_id)
        if burned:
            return burned
        return render_template("paste.html", data=fetch, paste_id=paste_id)
    if request.method == "POST":
        confirm(paste_id)
        return redirect("/")


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


@app.route("/u/<username>", methods=["POST", "GET"])
def profile(username):
    if request.method == "GET":
        user_pastes = public_pastes(username)
        info = about(username)
        pic = picture(username)
        return render_template("missing.html") if not user_pastes or username == "Anonymous" else \
            render_template("profile.html", pastes=user_pastes, info=about, pic=pic, username=username)
    if request.method == "POST":
        return redirect("/u/picture/" + username)


@app.route("/u/picture/<username>", methods=["POST", "GET"])
def edit_profile(username):
    if request.method == "GET":
        return render_template("picture.html", username=username) if session["username"] == username \
            else render_template("missing.html")
    if request.method == "POST":
        error = post_picture(username, request)
        if not error:
            return redirect("/u/" + username)
        else:
            return render_template("picture.html", error=error, username=username)


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


@app.route("/contact", methods=["POST", "GET"])
def contact_us():
    if request.method == "GET":
        return render_template("contact.html")
    if request.method == "POST":
        message = contact()
        return render_template("contact.html", message=message)
