import string
import random

from flask import request, session

from utils.db import db


def most_viewed():
    sql = "SELECT views, pasteid, title FROM pastes ORDER BY views DESC LIMIT 10"
    result = db.session.execute(sql)
    return result.fetchall()


def create_paste():
    paste_id = "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=8))
    content = request.form["paste"]
    if len(content) == 0:
        return "empty"
    title = content[:25]
    username = session.get("username", "Anonymous")
    sql = "INSERT INTO pastes (pasteid, paste, username, views, title) " \
          "VALUES (:pasteid, :paste, :username, 0, :title)"
    db.session.execute(sql, {"pasteid": paste_id, "paste": content, "username": username, "title": title})
    db.session.commit()
    return paste_id
