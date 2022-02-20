from flask import request

from utils.db import db


def contact():
    email = request.form["email"]
    if len(email) == 0:
        return "Contact information cannot be empty."
    message = request.form["message"]
    if len(message) == 0:
        return "Message cannot be empty."
    sql = "INSERT INTO contact (email, message) VALUES (:email, :message)"
    db.session.execute(sql, {"email": email, "message": message})
    db.session.commit()
    return "Message sent successfully!"


def delete_contact(number):
    sql = "DELETE FROM contact WHERE id=:id"
    db.session.execute(sql, {"id": number})
    db.session.commit()
