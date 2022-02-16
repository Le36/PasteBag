from flask import render_template

from modules.paste import paste, raw
from utils.db import db


def check_burn(paste_id):
    sql = "SELECT burn FROM pastes WHERE pasteid=:pasteid"
    result = db.session.execute(sql, {"pasteid": paste_id})
    fetched = result.fetchone()
    return render_template("burn.html", paste_id=paste_id) if fetched["burn"] else None


def burn(paste_id):
    fetch = raw(paste_id, True)
    if not fetch:
        return
    return fetch
