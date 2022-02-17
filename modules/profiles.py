from utils.db import db


def user_profile(username):
    sql = "SELECT V.views, P.paste_id, P.title, P.username FROM pastes P " \
          "LEFT JOIN paste_views V ON P.paste_id = V.paste_id " \
          "WHERE username=:username AND private=false ORDER BY views DESC"
    result = db.session.execute(sql, {"username": username})
    return result.fetchall()
