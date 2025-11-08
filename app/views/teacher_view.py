from flask import Blueprint, render_template, request, redirect, url_for
from controllers import teacher_controller as controller

teacher_bp = Blueprint('teacher_bp', __name__)

@teacher_bp.route("/teachers")
def index():
    teachers = controller.get_all_teachers()
    return render_template('teachers.html', teachers=teachers)

@teacher_bp.route("/teacher<int:teacher_id>")
def detail(teacher_id):
    a_teacher = controller.get_teacher_by_id(teacher_id)
    return render_template('teacher_detail.html', teacher=a_teacher)
