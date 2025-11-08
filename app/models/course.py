from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = 'student'

    course_id   =        db.Column(db.Integer, primary_key=True)
    course_name =        db.Column(db.String(50), nullable=False)
    description =        db.Column(db.String(50), nullable=False)
    credits =        db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Course, {self.course_name}, {self.credits}"
