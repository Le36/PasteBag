from base64 import b64encode
from zlib import decompress, compress

from utils.db import db


def public_pastes(username):
    sql = "SELECT V.views, P.paste_id, P.title, P.username FROM pastes P " \
          "LEFT JOIN paste_views V ON P.paste_id = V.paste_id " \
          "WHERE username=:username AND private=false ORDER BY views DESC"
    result = db.session.execute(sql, {"username": username})
    return result.fetchall()


def about(username):
    sql = "SELECT about FROM profile WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    return result.fetchone()


def post_about(username, request):
    info = request.form["about"]
    sql = "INSERT INTO profile (username,about) VALUES (:username,:about) " \
          "ON CONFLICT (username) DO UPDATE SET about = :about"
    db.session.execute(sql, {"username": username, "about": info})
    db.session.commit()


def picture(username):
    sql = "SELECT data FROM picture WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    try:
        data = result.fetchone()[0]
    except:
        return
    return b64encode(decompress(data)).decode("utf-8")


def post_picture(username, request):
    file = request.files["file"]
    name = file.filename
    if not name.endswith(".jpg"):
        return ".jpg required"
    data = file.read()
    if len(data) > 500 * 1024:
        return "max size 500 kB"
    data = compress(data)
    sql = "INSERT INTO picture (username,data) VALUES (:username,:data) " \
          "ON CONFLICT (username) DO UPDATE SET data = :data"
    db.session.execute(sql, {"username": username, "data": data})
    db.session.commit()
    return


def exists(username):
    sql = "SELECT username FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    return result.fetchone()
