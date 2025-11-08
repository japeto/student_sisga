#from flask_sqlalchemy import SQLAlchemy

#db = SQLAlchemy()

class Course(db.Model):
    __tablename__ = 'course'

    course_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    credits = db.Column(db.Integer, default=3)

    def __repr__(self):
        return f"Curso: {self.course_name}"