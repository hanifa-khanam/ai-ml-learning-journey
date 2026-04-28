CREATE DATABASE university_sys;
USE university_sys;

-- DDL
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    age INT CHECK (age >= 16)
);

CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    credits INT CHECK (credits > 0)
);

CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);


-- DML 
INSERT INTO students (student_id, name, email, age)
VALUES
(1, 'Alice Khan', 'alice.khan@example.com', 19),
(2, 'Bob Ali', 'bob.ali@example.com', 21),
(3, 'Sara Ahmed', 'sara.ahmed@example.com', 18);


INSERT INTO courses (course_id, course_name, credits)
VALUES 
(1, 'Data Structures', 3),
(2, 'Databases', 3),
(3, 'Python Programming', 4);

INSERT INTO enrollments(enrollment_id, student_id, course_id, enrollment_date)
VALUES
(1, 1, 1, '2026-02-01'),
(2, 1, 3, '2026-02-02'),
(3, 2, 2, '2026-02-03'),
(4, 3, 3, '2026-02-04');

UPDATE students
SET email = 'alice.new@gmail.com'
WHERE student_id = 1;

UPDATE courses
SET credits = 5
WHERE course_id = 3;

DELETE FROM enrollments
WHERE enrollment_id = 4;