-- Table: students
-- Stores personal information about each student.
-- Fiels:
--  id         - Unique identifier (auto-increment)
--  full_name  - Student's full name (required)
--  birth_year - Year of birth (required)
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    birth_year INTEGER NOT NULL
);

-- Table: grades
-- Stores grades for individual subjects per student.
-- Fields:
--   id         - Unique identifier (auto-increment)
--   student_id - Reference to students(id)
--   subject    - Name of the subject
--   grade      - Integer grade value (range 1–100)
CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    subject TEXT NOT NULL,
    grade INTEGER CHECK (grade BETWEEN 1 AND 100) NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students (id)
);

-- Insert students
INSERT INTO students (full_name, birth_year) VALUES
    ('Alice Johnson', 2005),
    ('Brian Smith', 2004),
    ('Carla Reyes', 2006),
    ('Daniel Kim', 2005),
    ('Eva Thompson', 2003),
    ('Felix Nguyen', 2007),
    ('Grace Patel', 2005),
    ('Henry Lopez', 2004),
    ('Isabella Martinez', 2006);

-- Insert grades
INSERT INTO grades (student_id, subject, grade) VALUES
    (1, 'Math', 88),
    (1, 'English', 92),
    (1, 'Science', 85),
    (2, 'Math', 75),
    (2, 'History', 83),
    (2, 'English', 79),
    (3, 'Science', 95),
    (3, 'Math', 91),
    (3, 'Art', 89),
    (4, 'Math', 84),
    (4, 'Science', 88),
    (4, 'Physical Education', 93),
    (5, 'English', 90),
    (5, 'History', 85),
    (5, 'Math', 88),
    (6, 'Science', 72),
    (6, 'Math', 78),
    (6, 'English', 81),
    (7, 'Art', 94),
    (7, 'Science', 87),
    (7, 'Math', 90),
    (8, 'History', 77),
    (8, 'Math', 83),
    (8, 'Science', 80),
    (9, 'English', 96),
    (9, 'Math', 89),
    (9, 'Art', 92);

-- Get all subjects and grades for Alice Johnson, ordered by grade
SELECT g.subject, g.grade
FROM students AS s
INNER JOIN grades AS g ON s.id = g.student_id
WHERE s.full_name = 'Alice Johnson'
ORDER BY g.grade DESC;

-- Average grade per student
SELECT s.full_name, ROUND(AVG(g.grade), 2) AS avg_grade
FROM students AS s
INNER JOIN grades AS g ON s.id = g.student_id
GROUP BY s.id, s.full_name
ORDER BY avg_grade DESC;

-- Students born after 2004
SELECT s.full_name, s.birth_year
FROM students AS s
WHERE s.birth_year > 2004
ORDER BY s.birth_year DESC;

-- Average grade per subject
SELECT g.subject, ROUND(AVG(g.grade), 2) AS avg_grade
FROM grades AS g
GROUP BY g.subject
ORDER BY avg_grade DESC;

-- Top 3 students with highest average grade
SELECT s.full_name, ROUND(AVG(g.grade), 2) AS avg_grade
FROM students AS s
INNER JOIN grades AS g ON s.id = g.student_id
GROUP BY s.id, s.full_name
ORDER BY avg_grade DESC
LIMIT 3;

-- Students who have at least one grade below 80
SELECT DISTINCT s.full_name
FROM students AS s
JOIN grades AS g ON s.id = g.student_id
WHERE g.grade < 80
ORDER BY s.full_name;
