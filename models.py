from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Result(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    visual = db.Column(db.Float)

    auditory = db.Column(db.Float)

    kinesthetic = db.Column(db.Float)

    dominant = db.Column(db.String(50))