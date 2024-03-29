from app import app
from flask import render_template, request, redirect, session
from modules.accounts import user_login, user_logout, user_register, check_csrf, paste_csrf
from modules.admin import all_pastes, all_contacts
from modules.burn import check_burn, burn
from modules.contact import contact, delete_contact
from modules.front import most_viewed, create_paste

from modules.paste import paste, raw, confirm
from modules.profiles import public_pastes, about, picture, post_picture, exists, post_about


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
        check_csrf()
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
        if not exists(username) or username == "Anonymous":
            return render_template("missing.html")
        user_pastes = public_pastes(username)
        info = about(username)
        pic = picture(username)
        return render_template("profile.html", pastes=user_pastes, data=info, pic=pic, username=username)
    if request.method == "POST":
        if request.form.get("picture"):
            return redirect("/u/picture/" + username)
        if request.form.get("about"):
            return redirect("/u/about/" + username)


@app.route("/u/picture/<username>", methods=["POST", "GET"])
def edit_picture(username):
    if request.method == "GET":
        return render_template("picture.html", username=username) if session["username"] == username \
            else render_template("missing.html")
    if request.method == "POST":
        check_csrf()
        error = post_picture(username, request)
        if not error:
            return redirect("/u/" + username)
        else:
            return render_template("picture.html", error=error, username=username)


@app.route("/u/about/<username>", methods=["POST", "GET"])
def edit_about(username):
    if request.method == "GET":
        return render_template("about.html", username=username) if session["username"] == username \
            else render_template("missing.html")
    if request.method == "POST":
        check_csrf()
        post_about(username, request)
        return redirect("/u/" + username)


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


@app.route("/admin", methods=["POST", "GET"])
def admin():
    if request.method == "GET":
        if session.get("admin"):
            pastes = all_pastes()
            return render_template("admin.html", pastes=pastes)
        else:
            return render_template("missing.html")
    if request.method == "POST":
        if session.get("admin"):
            return redirect("/admin2")
        else:
            return render_template("missing.html")


@app.route("/admin2", methods=["POST", "GET"])
def admin2():
    if request.method == "GET":
        if session.get("admin"):
            contacts = all_contacts()
            return render_template("admin2.html", contacts=contacts)
        else:
            return render_template("missing.html")
    if request.method == "POST":
        if session.get("admin"):
            return redirect("/admin")
        else:
            return render_template("missing.html")


@app.route("/admin2/delete/<number>", methods=["GET"])
def admin2_delete(number):
    if request.method == "GET":
        if session.get("admin"):
            delete_contact(number)
            return redirect("/admin2")
        else:
            return render_template("missing.html")
