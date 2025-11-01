# 📘 SISGA — Sistema de Gestión Académica

SISGA (Sistema de Gestión Académica) es una base de datos diseñada para administrar la información académica de estudiantes, docentes y cursos.  
El sistema permite registrar estudiantes y profesores, asignar cursos, y gestionar las matrículas y calificaciones.

---

## 🏗️ Estructura General

El proyecto está compuesto por las siguientes entidades principales:

- **student** → Información básica de los estudiantes.  
- **teacher** → Información básica de los docentes.  
- **course** → Catálogo de cursos disponibles.  
- **enroll** → Relación entre estudiantes y cursos (matrículas).  
- **teach** → Relación entre docentes y cursos (asignaciones).

---

## 🧱 Esquema de Tablas

### 🧑‍🎓 `student`
| Campo | Tipo | Descripción |
|--------|------|-------------|
| `student_id` | SERIAL PRIMARY KEY | Identificador único del estudiante |
| `first_name` | VARCHAR(50) | Nombre |
| `last_name` | VARCHAR(50) | Apellido |
| `email` | VARCHAR(100) UNIQUE | Correo institucional |
| `enrollment_date` | DATE | Fecha de inscripción |

---

### 👨‍🏫 `teacher`
| Campo | Tipo | Descripción |
|--------|------|-------------|
| `teacher_id` | SERIAL PRIMARY KEY | Identificador único del docente |
| `first_name` | VARCHAR(50) | Nombre |
| `last_name` | VARCHAR(50) | Apellido |
| `email` | VARCHAR(100) UNIQUE | Correo institucional |
| `hire_date` | DATE | Fecha de contratación |

---

### 📚 `course`
| Campo | Tipo | Descripción |
|--------|------|-------------|
| `course_id` | SERIAL PRIMARY KEY | Identificador único del curso |
| `course_name` | VARCHAR(100) | Nombre del curso |
| `description` | TEXT | Descripción del curso |
| `credits` | INT DEFAULT 3 | Créditos académicos |

---

### 🧾 `enroll`
**Relación muchos a muchos entre estudiantes y cursos.**

| Campo | Tipo | Descripción |
|--------|------|-------------|
| `eid` | INT PRIMARY KEY | Identificador de la matrícula |
| `student_id` | INT | Referencia al estudiante |
| `course_id` | INT | Referencia al curso |
| `grade` | DECIMAL(4,2) | Nota obtenida |
| `enrollment_date` | DATE DEFAULT CURRENT_DATE | Fecha de matrícula |

🔗 **Claves foráneas:**
- `student_id` → `student(student_id)`  
- `course_id` → `course(course_id)`

---

### 🧑‍🏫 `teach`
**Relación muchos a muchos entre docentes y cursos.**

| Campo | Tipo | Descripción |
|--------|------|-------------|
| `teacher_id` | INT | Referencia al docente |
| `course_id` | INT | Referencia al curso |
| `assignment_date` | DATE DEFAULT CURRENT_DATE | Fecha de asignación |

🔗 **Claves foráneas:**
- `teacher_id` → `teacher(teacher_id)`  
- `course_id` → `course(course_id)`

---

## 🔍 Relaciones entre Tablas

