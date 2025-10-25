from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = 'student'

    student_id =        db.Column(db.Integer, primary_key=True)
    first_name =        db.Column(db.String(50), nullable=False)
    last_name =         db.Column(db.String(50), nullable=False)
    email =             db.Column(db.String(100), unique=True, nullable=False)
    enrollment_date =   db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f"Soy, {self.first_name}, {self.last_name}"
