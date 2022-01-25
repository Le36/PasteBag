from app import app
from flask import render_template, request, redirect, session
from db import db
from werkzeug.security import check_password_hash, generate_password_hash


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        return redirect("/")


@app.route("/logout")
def logout():
    return redirect("/")
