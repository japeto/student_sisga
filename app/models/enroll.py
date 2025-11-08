#from flask_sqlalchemy import SQLAlchemy

#db = SQLAlchemy()


class Enroll(db.Model):
    __tablename__ = 'enroll'

    eid = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id', ondelete='CASCADE'))
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id', ondelete='CASCADE'))
    grade = db.Column(db.Numeric(4, 2), nullable=False)
    enrollment_date = db.Column(db.Date, default=db.func.current_date())

    student = db.relationship('Student', backref=db.backref('enrollments', cascade='all, delete'))
    course = db.relationship('Course', backref=db.backref('enrollments', cascade='all, delete'))

    def __repr__(self):
        return f"Inscripción {self.eid}: Estudiante {self.student_id} en Curso {self.course_id}"
