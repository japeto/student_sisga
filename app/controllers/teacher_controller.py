from models.teacher import db, Teacher

# CREATE
def create_teacher(first_name, last_name, email, hire_date):
    a_teacher = Teacher(first_name=first_name, last_name=last_name, email=email, hire_date=hire_date)
    db.session.add(a_teacher)
    db.session.commit()
    return a_teacher

# READ
def get_all_teachers():
    return Teacher.query.all()

def get_teacher_by_id(teacher_id):
    return Teacher.query.get(teacher_id)

# UPDATE
def update_teacher_by_id(teacher_id, first_name, last_name, email):
    a_teacher = Teacher.query.get(teacher_id)
    if a_teacher:
        a_teacher.first_name = first_name
        a_teacher.last_name = last_name
        a_teacher.email = email
        db.session.commit()
    return a_teacher

# DELETE
def delete_teacher(teacher_id):
    a_teacher = Teacher.query.get(teacher_id)
    if a_teacher:
        db.session.delete(a_teacher)
        db.session.commit()
    return a_teacher
