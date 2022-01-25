from app import app
from flask import render_template, request, redirect
from db import db


@app.route("/")
def index():
    return render_template("index.html")
