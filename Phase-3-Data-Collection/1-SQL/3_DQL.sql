-- Retrieve all student names and emails
SELECT name, email
FROM students;

-- Students aged 18 or older
SELECT *
FROM students
WHERE age >= 18;

-- Students aged between 18 and 22 OR name starts with 'A'
SELECT *
FROM students
WHERE (age BETWEEN 18 AND 22) OR name LIKE 'A%';


-- List unique course credits
SELECT DISTINCT credits
FROM courses;


-- Students whose name contains 'an'
SELECT *
FROM students
WHERE name LIKE '%an%';


-- Courses with course_id 1, 2, or 3
SELECT *
FROM courses
WHERE course_id IN (1, 2, 3);



-- Students aged 18 to 25
SELECT *
FROM students
WHERE age BETWEEN 18 AND 25;


-- Students without email
SELECT *
FROM students
WHERE email IS NULL;


-- Rename output column
SELECT name AS student_name, age AS student_age
FROM students;


-- List students by age descending
SELECT *
FROM students
ORDER BY age DESC;



-- Count students per age
SELECT age, COUNT(*) AS student_count
FROM students
GROUP BY age;


-- Ages with more than 1 student
SELECT age, COUNT(*) AS student_count
FROM students
GROUP BY age
HAVING COUNT(*) > 1;


-- Total courses, average credits, max/min credits
SELECT 
    COUNT(*) AS total_courses,
    AVG(credits) AS avg_credits,
    MAX(credits) AS max_credits,
    MIN(credits) AS min_credits
FROM courses;