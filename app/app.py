import os
from flask import Flask
from models.student import db
from views.student_view import student_bp

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql://sisga_user:sisga_pass@sisga_database:5432/sisga_db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "Est4esUn411aVeSecR3t4"

app = Flask(__name__)
db.init_app(app)

app.register_blueprint(student_bp)

if __name__ == '__main__':
    with app.app_context():
        db.reflect()
    app.run(debug=True)