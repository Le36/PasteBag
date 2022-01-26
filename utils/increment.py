from db import db


def increment(paste_id):
    sql = "SELECT pastes FROM pastes WHERE pasteid=:pasteid"
    result = db.session.execute(sql, {"pasteid": paste_id})
    fetched = result.fetchone()
    sql = "UPDATE pastes SET views = views + 1 WHERE pasteid=:pasteid"
    db.session.execute(sql, {"pasteid": paste_id})
    db.session.commit()
