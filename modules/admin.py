from utils.db import db


def all_pastes():
    sql = "SELECT V.views, P.paste_id, P.title, P.username, P.private, P.burn FROM pastes P " \
          "LEFT JOIN paste_views V ON P.paste_id = V.paste_id ORDER BY views DESC"
    result = db.session.execute(sql)
    return result.fetchall()


def all_contacts():
    sql = "SELECT id, email, message FROM contact"
    result = db.session.execute(sql)
    return result.fetchall()
