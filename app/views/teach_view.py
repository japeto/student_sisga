from flask import Blueprint, render_template, request, redirect, url_for
from controllers import teach_controller as controller

teach_bp = Blueprint('teach_bp', __name__)

@teach_bp.route("/assignments")
def index():
    assignments = controller.get_all_assignments()
    return render_template('assignments.html', assignments=assignments)

@teach_bp.route("/assignment/<int:teacher_id>/<int:course_id>")
def detail(teacher_id, course_id):
    a_assignment = controller.get_assignment(teacher_id, course_id)
    return render_template('assignment_detail.html', assignment=a_assignment)
