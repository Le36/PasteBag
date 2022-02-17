from flask import make_response, session

from utils.db import db
from utils.increment import increment


def paste(paste_id):
    sql = "SELECT P.paste, P.username, V.views, P.title, P.burn, P.syntax, P.time " \
          "FROM pastes P LEFT JOIN paste_views V ON P.paste_id = V.paste_id WHERE P.paste_id=:paste_id"
    result = db.session.execute(sql, {"paste_id": paste_id})
    fetched = result.fetchone()
    if not fetched:
        return
    increment(paste_id)
    return fetched


def raw(paste_id, burn):
    sql = "SELECT paste, burn FROM pastes WHERE paste_id=:paste_id"
    result = db.session.execute(sql, {"paste_id": paste_id})
    fetched = result.fetchone()
    if not fetched:
        return
    increment(paste_id)
    response = make_response(fetched["paste"], 200)
    response.mimetype = "text/plain"
    remove(paste_id) if burn and fetched["burn"] else None
    return response


def remove(paste_id):
    sql = "DELETE FROM pastes WHERE paste_id=:paste_id"
    db.session.execute(sql, {"paste_id": paste_id})
    db.session.commit()


def confirm(paste_id):
    sql = "SELECT username FROM pastes WHERE paste_id=:paste_id"
    result = db.session.execute(sql, {"paste_id": paste_id})
    fetched = result.fetchone()
    if fetched["username"] == session["username"]:
        remove(paste_id)
