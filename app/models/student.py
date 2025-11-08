#from flask_sqlalchemy import SQLAlchemy
#db = SQLAlchemy()
from . import db

class Student(db.Model):
    __tablename__ = 'student'

    student_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(100), unique=True, nullable=True)
    enrollment_date = db.Column(db.Date, nullable=True)

    def __repr__(self):
        return f"Soy {self.first_name} {self.last_name}"
