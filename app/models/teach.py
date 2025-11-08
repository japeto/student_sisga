#from flask_sqlalchemy import SQLAlchemy
#db = SQLAlchemy()
from . import db

class Teach(db.Model):
    __tablename__ = 'teach'

    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.teacher_id', ondelete='CASCADE'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id', ondelete='CASCADE'), primary_key=True)
    assignment_date = db.Column(db.Date, default=db.func.current_date())

    teacher = db.relationship('Teacher', backref=db.backref('courses_assigned', cascade='all, delete'))
    course = db.relationship('Course', backref=db.backref('teachers_assigned', cascade='all, delete'))

    def __repr__(self):
        return f"Profesor {self.teacher_id} asignado al curso {self.course_id}"