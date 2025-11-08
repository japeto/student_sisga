from models.teach import db, Teach

# CREATE
def assign_teacher_to_course(teacher_id, course_id, assignment_date=None):
    a_teach = Teach(teacher_id=teacher_id, course_id=course_id, assignment_date=assignment_date)
    db.session.add(a_teach)
    db.session.commit()
    return a_teach

# READ
def get_all_assignments():
    return Teach.query.all()

def get_assignment(teacher_id, course_id):
    return Teach.query.filter_by(teacher_id=teacher_id, course_id=course_id).first()

# UPDATE
def update_assignment_date(teacher_id, course_id, new_date):
    a_teach = Teach.query.filter_by(teacher_id=teacher_id, course_id=course_id).first()
    if a_teach:
        a_teach.assignment_date = new_date
        db.session.commit()
    return a_teach

# DELETE
def delete_assignment(teacher_id, course_id):
    a_teach = Teach.query.filter_by(teacher_id=teacher_id, course_id=course_id).first()
    if a_teach:
        db.session.delete(a_teach)
        db.session.commit()
    return a_teach
