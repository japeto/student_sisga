from models.course import db, course
from datetime import datetime

def create_course(course_name, description, credits):
    a_course = course(course_name=course_name, description=description, credits=credits)
    db.session.add(a_course)
    db.session.commit()
    return a_course

# READ
def get_all_courses():
    return course.query.all()

def get_course_byid(course_id):
    return course.query.get(course_id)

# UPDATE
def update_course_byid(course_id, course_name, description, credits):
    a_course = course.query.get(course_id)
    a_course.course_name = course_name
    a_course.description = description
    a_course.credits = credits
    db.session.commit()
    return a_course

def update_course_byemail(course_name, description, credits):
    a_course = course.query.filter(course.course_name==course_name)
    a_course.description=description
    a_course.credits=credits
    db.session.commit()
    return a_course
    
# DELETE
def delete_course(course_id):
    a_course = course.query.get(course_id)
    # Not implemented yet
    return a_course