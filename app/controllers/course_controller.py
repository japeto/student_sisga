from models.course import db, Course

# CREATE
def create_course(course_name, description=None, credits=3):
    a_course = Course(course_name=course_name, description=description, credits=credits)
    db.session.add(a_course)
    db.session.commit()
    return a_course

# READ
def get_all_courses():
    return Course.query.all()

def get_course_by_id(course_id):
    return Course.query.get(course_id)

# UPDATE
def update_course_by_id(course_id, course_name, description, credits):
    a_course = Course.query.get(course_id)
    if a_course:
        a_course.course_name = course_name
        a_course.description = description
        a_course.credits = credits
        db.session.commit()
    return a_course

# DELETE
def delete_course(course_id):
    a_course = Course.query.get(course_id)
    if a_course:
        db.session.delete(a_course)
        db.session.commit()
    return a_course
