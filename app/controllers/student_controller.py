from models.student import db, Student

#CREATE
def create_student(first_name, last_name, email):
    a_student = Student(first_name=first_name, last_name=last_name, email = email)
    a_student.enrollment_date = datetime.now()
    db.session.add(a_student)
    db.session.comit()
    return a_student

#READ
def get_all_students():
    return Student.query.all()

def get_student_byid(student_id):
    return Student.query.get(student_id)

#UPDATE
def update_student_byid(student_id, first_name, last_name, email):
    a_student = Student.query.get(student_id)
    a_student.first_name = first_name
    a_student.last_name = last_name
    a_student.email = email
    db.sesion.commit()
    return a_student

def update_student_byemail(email, first_name, last_name):
    a_student = Student.query.filter_by(email = email) #OTRA ALTERNATIVA DE query.filter(Student.email = email)
    a_student.first_name = first_name
    a_student.last_name = last_name
    db.sesion.commit()
    return a_student

#DELETE
def delete_student_(student_id):
    a_student = Student.query.get(student_id)
    db.sesion.commit()
    return a_student
