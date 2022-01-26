from flask import make_response

from utils.db import db
from utils.increment import increment


def paste(paste_id):
    sql = "SELECT paste, username, views, title FROM pastes WHERE pasteid=:pasteid"
    result = db.session.execute(sql, {"pasteid": paste_id})
    fetched = result.fetchone()
    if not fetched:
        return
    increment(paste_id)
    return fetched


def raw(paste_id):
    sql = "SELECT paste FROM pastes WHERE pasteid=:pasteid"
    result = db.session.execute(sql, {"pasteid": paste_id})
    fetched = result.fetchone()
    if not fetched:
        return
    from utils.increment import increment
    increment(paste_id)
    response = make_response(fetched["paste"], 200)
    response.mimetype = "text/plain"
    return response
