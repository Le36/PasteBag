from utils.db import db


def increment(paste_id):
    sql = "INSERT INTO paste_views (paste_id, views) VALUES (:paste_id, 1) " \
          "ON CONFLICT (paste_id) DO UPDATE SET views = paste_views.views + 1"
    db.session.execute(sql, {"paste_id": paste_id})
    db.session.commit()
