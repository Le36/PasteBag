import string
import random

from flask import request, session

from utils.db import db


def most_viewed():
    sql = "SELECT views, pasteid, title FROM pastes WHERE private=false ORDER BY views DESC LIMIT 10"
    result = db.session.execute(sql)
    return result.fetchall()


def create_paste():
    content = request.form["paste"]
    if len(content) == 0:
        return "empty"
    private = True if request.form["visibility"] == "Private" else False
    burn = True if request.form.get("burn") == "on" else False
    paste_id = "".join(
        random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=80 if private else 8))
    title = content[:25]
    username = session.get("username", "Anonymous")
    sql = "INSERT INTO pastes (pasteid, paste, username, views, title, private, burn) " \
          "VALUES (:pasteid, :paste, :username, 0, :title, :private, :burn)"
    db.session.execute(sql,
                       {"pasteid": paste_id, "paste": content, "username": username, "title": title, "private": private,
                        "burn": burn})
    db.session.commit()
    return paste_id
