from models.enroll import db, Enroll

# CREATE
def create_enroll(student_id, course_id, grade, enrollment_date=None):
    a_enroll = Enroll(student_id=student_id, course_id=course_id, grade=grade, enrollment_date=enrollment_date)
    db.session.add(a_enroll)
    db.session.commit()
    return a_enroll

# READ
def get_all_enrollments():
    return Enroll.query.all()

def get_enroll_by_id(eid):
    return Enroll.query.get(eid)

# UPDATE
def update_enroll_by_id(eid, grade):
    a_enroll = Enroll.query.get(eid)
    if a_enroll:
        a_enroll.grade = grade
        db.session.commit()
    return a_enroll

# DELETE
def delete_enroll(eid):
    a_enroll = Enroll.query.get(eid)
    if a_enroll:
        db.session.delete(a_enroll)
        db.session.commit()
    return a_enroll
