# server/models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140), nullable=False)
    username = db.Column(db.String(64), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __repr__(self):
        return f"Message('{self.body}', '{self.username}')"