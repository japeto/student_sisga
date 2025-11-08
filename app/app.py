import os
from flask import Flask
from models import db
from views.student_view import student_bp
from views.teacher_view import teacher_bp
from views.course_view import course_bp
from views.enroll_view import enroll_bp
from views.teach_view import teach_bp
from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy() # db intitialized here
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://sisga_user:sisga_pass@sisga_db:5432/sisga"
db.init_app(app)

app.register_blueprint(student_bp)
app.register_blueprint(teacher_bp)
app.register_blueprint(course_bp)
app.register_blueprint(enroll_bp)
app.register_blueprint(teach_bp)

if __name__ == '__main__':
    with app.app_context():
        db.reflect()
    app.run(debug=True)