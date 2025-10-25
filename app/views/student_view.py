from flask import Blueprint, render_template, request, redirect, url_for
# De la carpeta controllers, importe todo lo que hay en student_controller
# con alias controller
from controllers import student_controller as controller

student_bp =Blueprint('student_bp', __name__)

@student_bp.route("/")
def index():
    students = controller.get_all_students()
    return render_template('students.html', students=students)

@student_bp.route("/student/<int:student_id>")
def detail(student_id):
    a_student = controller.get_student_byid(student_id)
    return render_template('student_detail.html', student=a_student)
