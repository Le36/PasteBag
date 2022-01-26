from utils.db import db


def user_profile(username):
    sql = "SELECT views, pasteid, title, username FROM pastes WHERE username=:username ORDER BY views DESC"
    result = db.session.execute(sql, {"username": username})
    return result.fetchall()
