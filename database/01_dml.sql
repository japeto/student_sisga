-- ==========================================
-- INSERTS: student
-- ==========================================
INSERT INTO student (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Emma', 'Smith', 'emma.smith@example.com', '2023-09-02'),
('Liam', 'Johnson', 'liam.johnson@example.com', '2023-09-03'),
('Olivia', 'Brown', 'olivia.brown@example.com', '2023-09-04'),
('Noah', 'Williams', 'noah.williams@example.com', '2023-09-05'),
('Ava', 'Jones', 'ava.jones@example.com', '2023-09-06'),
('Ethan', 'Garcia', 'ethan.garcia@example.com', '2023-09-07'),
('Sophia', 'Miller', 'sophia.miller@example.com', '2023-09-08'),
('Mason', 'Davis', 'mason.davis@example.com', '2023-09-09'),
('Isabella', 'Martinez', 'isabella.martinez@example.com', '2023-09-10');

-- ==========================================
-- INSERTS: teacher
-- ==========================================
INSERT INTO teacher (first_name, last_name, email, hire_date) VALUES
('Michael', 'Anderson', 'michael.anderson@university.com', '2020-08-15'),
('Sarah', 'Clark', 'sarah.clark@university.com', '2019-06-01'),
('David', 'Rodriguez', 'david.rodriguez@university.com', '2021-02-20'),
('Laura', 'Lewis', 'laura.lewis@university.com', '2018-03-10'),
('James', 'Walker', 'james.walker@university.com', '2022-01-05'),
('Emily', 'Hall', 'emily.hall@university.com', '2020-09-14'),
('Robert', 'Allen', 'robert.allen@university.com', '2017-11-23'),
('Jessica', 'Young', 'jessica.young@university.com', '2021-07-30'),
('William', 'Hernandez', 'william.hernandez@university.com', '2019-10-18'),
('Karen', 'King', 'karen.king@university.com', '2018-12-01');

-- ==========================================
-- INSERTS: course
-- ==========================================
INSERT INTO course (course_name, description, credits) VALUES
('Introduction to Computer Science', 'Basic programming and computer concepts.', 4),
('Database Systems', 'Relational models, SQL, and database design.', 3),
('Data Structures', 'Study of algorithms and data organization.', 3),
('Web Development', 'Front-end and back-end web technologies.', 3),
('Artificial Intelligence', 'Principles and applications of AI.', 4),
('Software Engineering', 'Software lifecycle and project management.', 3),
('Operating Systems', 'Concepts of OS design and implementation.', 4),
('Computer Networks', 'Network protocols, architectures, and security.', 3),
('Mobile App Development', 'Developing applications for Android/iOS.', 3),
('Cybersecurity Fundamentals', 'Principles of computer and network security.', 3);

-- ==========================================
-- INSERTS: student_course
-- ==========================================
INSERT INTO enroll (student_id, course_id, grade, enrollment_date) VALUES
(1, 1, 3.50, '2023-09-01'),
(1, 2, 2.00, '2023-09-02'),
(2, 3, 4.25, '2023-09-03'),
(3, 1, 4.00, '2023-09-04'),
(3, 4, 3.00, '2023-09-05'),
(4, 5, 3.75, '2023-09-06'),
(5, 2, 4.50, '2023-09-07'),
(6, 6, 3.00, '2023-09-08'),
(7, 3, 4.50, '2023-09-09'),
(8, 7, 5.00, '2023-09-10');

-- ==========================================
-- INSERTS: teacher_course
-- ==========================================
INSERT INTO teach (teacher_id, course_id, assignment_date) VALUES
(1, 1, '2023-01-10'),
(1, 2, '2023-01-10'),
(2, 3, '2023-02-01'),
(3, 4, '2023-02-05'),
(4, 5, '2023-03-01'),
(5, 6, '2023-03-15'),
(6, 7, '2023-04-01'),
(7, 8, '2023-04-10'),
(8, 9, '2023-05-01'),
(9, 10, '2023-05-10');