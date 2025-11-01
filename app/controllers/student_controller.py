## De la carpeta models, desde el archivo student
## importar db(conexion a la base de datos) y Student (La clase que representa los estudiantes)
from models.student import db, Student
## importar la fecha y tiempo actual
from datetime import datetime

# CREATE
## def: para definir una funcion
## create_student, nombre de la funcion
## parametros: first_name, last_name, email
def create_student(first_name, last_name, email):
    """
    Crea un estudiante con sus nombres, apellidos y correo
    @param first_name Nombres del estudiante
    @param last_name Apellidos del estudiante
    @param email Correo del estudiante

    @return Un estudiante nuevo
    """
    a_student = Student(first_name=first_name, last_name=last_name, email=email)
    a_student.enrollment_date = datetime.now()
    db.session.add(a_student)
    db.session.commit()
    return a_student

# READ
def get_all_students():
    return Student.query.all()

def get_student_byid(student_id):
    return Student.query.get(student_id)

# UPDATE
def update_student_byid(student_id, first_name, last_name, email):
    a_student = Student.query.get(student_id)
    a_student.first_name=first_name
    a_student.last_name=last_name
    a_student.email=email
    db.session.commit()
    return a_student

def update_student_byemail(email, first_name, last_name):
    a_student = Student.query.filter(Student.email==email)
    a_student.first_name=first_name
    a_student.last_name=last_name
    db.session.commit()
    return a_student
    
# DELETE
def delete_student(student_id):
    a_student = Student.query.get(student_id)
    # Not implemented yet
    return a_student