from models.teacher import db, teacher
from datetime import datetime

def create_teacher(first_name, last_name, email):
    a_teacher = teacher(first_name=first_name, last_name=last_name, email=email)
    a_teacher.enrollment_date = datetime.now()
    db.session.add(a_teacher)
    db.session.commit()
    return a_teacher

# READ
def get_all_teachers():
    return teacher.query.all()

def get_teacher_byid(teacher_id):
    return teacher.query.get(teacher_id)

# UPDATE
def update_teacher_byid(teacher_id, first_name, last_name, email):
    a_teacher = teacher.query.get(teacher_id)
    a_teacher.first_name=first_name
    a_teacher.last_name=last_name
    a_teacher.email=email
    db.session.commit()
    return a_teacher

def update_teacher_byemail(email, first_name, last_name):
    a_teacher = teacher.query.filter(teacher.email==email)
    a_teacher.first_name=first_name
    a_teacher.last_name=last_name
    db.session.commit()
    return a_teacher
    
# DELETE
def delete_teacher(teacher_id):
    a_teacher = teacher.query.get(teacher_id)
    # Not implemented yet
    return a_teacher