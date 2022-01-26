from db import db


def increment(paste_id):
    sql = "UPDATE pastes SET views = views + 1 WHERE pasteid=:pasteid"
    db.session.execute(sql, {"pasteid": paste_id})
    db.session.commit()
