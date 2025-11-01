import os
from flask import Flask
from models.student import db
from views.student_view import student_bp
from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy() # db intitialized here
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://sisga_user:sisga_pass@localhost:5432/sisga"
db.init_app(app)

app.register_blueprint(student_bp)

if __name__ == '__main__':
    with app.app_context():
        db.reflect()
    app.run(debug=True)