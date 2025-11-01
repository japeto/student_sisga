-- Create table: student
CREATE TABLE student (
    student_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    enrollment_date DATE NOT NULL
);

-- Create table: teacher
CREATE TABLE teacher (
    teacher_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    hire_date DATE NOT NULL
);

-- Create table: course
CREATE TABLE course (
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    description TEXT,
    credits INT DEFAULT 3
);

-- Many-to-many: student ↔ course
CREATE TABLE enroll (
    eid SERIAL PRIMARY KEY,
    student_id INT,
    course_id INT,
    grade DECIMAL(4,2) NOT NULL,
    enrollment_date DATE DEFAULT CURRENT_DATE,
    UNIQUE(student_id, course_id, enrollment_date),
    FOREIGN KEY (student_id) REFERENCES student(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES course(course_id) ON DELETE CASCADE
);

-- Many-to-many: teacher ↔ course
CREATE TABLE teach (
    teacher_id INT,
    course_id INT,
    assignment_date DATE DEFAULT CURRENT_DATE,
    PRIMARY KEY (teacher_id, course_id),
    FOREIGN KEY (teacher_id) REFERENCES teacher(teacher_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES course(course_id) ON DELETE CASCADE
);
