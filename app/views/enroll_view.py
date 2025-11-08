from flask import Blueprint, render_template, request, redirect, url_for
from controllers import enroll_controller as controller

enroll_bp = Blueprint('enroll_bp', __name__)

@enroll_bp.route("/enrollments")
def index():
    enrollments = controller.get_all_enrollments()
    return render_template('enrollments.html', enrollments=enrollments)

@enroll_bp.route("/enroll<int:eid>")
def detail(eid):
    a_enroll = controller.get_enroll_by_id(eid)
    return render_template('enroll_detail.html', enroll=a_enroll)
