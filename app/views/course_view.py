from flask import Blueprint, render_template, request, redirect, url_for
from controllers import course_controller as controller

course_bp = Blueprint('course_bp', __name__)

@course_bp.route("/courses")
def index():
    courses = controller.get_all_courses()
    return render_template('courses.html', courses=courses)

@course_bp.route("/course<int:course_id>")
def detail(course_id):
    a_course = controller.get_course_by_id(course_id)
    return render_template('course_detail.html', course=a_course)
