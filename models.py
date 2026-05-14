from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Result(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(db.String(100))

    student_class = db.Column(db.String(50))

    gender = db.Column(db.String(20))

    visual = db.Column(db.Float)

    auditory = db.Column(db.Float)

    kinesthetic = db.Column(db.Float)

    dominant = db.Column(db.String(50))