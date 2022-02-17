from flask import make_response, session

from utils.db import db
from utils.increment import increment


def paste(paste_id):
    sql = "SELECT paste, username, views, title, burn, syntax FROM pastes WHERE pasteid=:pasteid"
    result = db.session.execute(sql, {"pasteid": paste_id})
    fetched = result.fetchone()
    if not fetched:
        return
    increment(paste_id)
    return fetched


def raw(paste_id, burn):
    sql = "SELECT paste, burn FROM pastes WHERE pasteid=:pasteid"
    result = db.session.execute(sql, {"pasteid": paste_id})
    fetched = result.fetchone()
    if not fetched:
        return
    increment(paste_id)
    response = make_response(fetched["paste"], 200)
    response.mimetype = "text/plain"
    remove(paste_id) if burn and fetched["burn"] else None
    return response


def remove(paste_id):
    sql = "DELETE FROM pastes WHERE pasteid=:pasteid"
    db.session.execute(sql, {"pasteid": paste_id})
    db.session.commit()


def confirm(paste_id):
    sql = "SELECT username FROM pastes WHERE pasteid=:pasteid"
    result = db.session.execute(sql, {"pasteid": paste_id})
    fetched = result.fetchone()
    if fetched["username"] == session["username"]:
        remove(paste_id)
