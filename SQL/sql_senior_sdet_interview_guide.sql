/*
============================================================
SQL INTERVIEW GUIDE – Senior SDET / Automation Engineer
============================================================

This file covers:

1. Basics
2. Filtering & Sorting
3. Joins
4. Aggregations (GROUP BY, HAVING)
5. Subqueries
6. Window Functions
7. CASE Statements
8. Duplicates Handling
9. Nth Highest Salary Problems
10. Real Automation Testing Scenarios
11. Indexing Basics
12. ACID & Transactions
============================================================
*/


/*============================================================
1. BASIC SELECT
============================================================*/

-- Get all employees
SELECT * FROM employees;

-- Select specific columns
SELECT name, salary
FROM employees;


/*============================================================
2. FILTERING & SORTING
============================================================*/

-- Employees earning more than 50000
SELECT name, salary
FROM employees
WHERE salary > 50000;

-- Sort by salary descending
SELECT name, salary
FROM employees
ORDER BY salary DESC;

-- Limit results (Top 5 highest salaries)
SELECT name, salary
FROM employees
ORDER BY salary DESC
LIMIT 5;


/*============================================================
3. JOINS (VERY IMPORTANT FOR SENIOR ROLES)
============================================================*/

-- Tables:
-- employees(id, name, dept_id, salary)
-- departments(id, dept_name)

-- INNER JOIN (only matching records)
SELECT e.name, d.dept_name
FROM employees e
INNER JOIN departments d
ON e.dept_id = d.id;

-- LEFT JOIN (all employees even if no department)
SELECT e.name, d.dept_name
FROM employees e
LEFT JOIN departments d
ON e.dept_id = d.id;

-- Employees without department
SELECT e.name
FROM employees e
LEFT JOIN departments d
ON e.dept_id = d.id
WHERE d.id IS NULL;


/*============================================================
4. GROUP BY & HAVING (AGGREGATIONS)
============================================================*/

-- Count employees per department
SELECT dept_id, COUNT(*) AS total_employees
FROM employees
GROUP BY dept_id;

-- Departments with more than 5 employees
SELECT dept_id, COUNT(*) AS total
FROM employees
GROUP BY dept_id
HAVING COUNT(*) > 5;

-- Average salary per department
SELECT dept_id, AVG(salary) AS avg_salary
FROM employees
GROUP BY dept_id;


/*============================================================
5. SUBQUERIES
============================================================*/

-- Employees earning more than Adam
SELECT name, salary
FROM employees
WHERE salary > (
    SELECT salary
    FROM employees
    WHERE name = 'Adam'
);

-- Second highest salary (subquery method)
SELECT MAX(salary)
FROM employees
WHERE salary < (
    SELECT MAX(salary)
    FROM employees
);


/*============================================================
6. WINDOW FUNCTIONS (SENIOR LEVEL TOPIC)
============================================================*/

-- Assign row number based on salary
SELECT name, salary,
       ROW_NUMBER() OVER (ORDER BY salary DESC) AS row_num
FROM employees;

-- Dense rank (handles ties)
SELECT name, salary,
       DENSE_RANK() OVER (ORDER BY salary DESC) AS rank
FROM employees;

-- Get 2nd highest salary using window function
SELECT name, salary
FROM (
    SELECT name, salary,
           ROW_NUMBER() OVER (ORDER BY salary DESC) AS rn
    FROM employees
) t
WHERE rn = 2;


/*============================================================
7. CASE STATEMENTS (Conditional Logic)
============================================================*/

SELECT name, salary,
CASE
    WHEN salary > 80000 THEN 'High'
    WHEN salary BETWEEN 50000 AND 80000 THEN 'Medium'
    ELSE 'Low'
END AS salary_category
FROM employees;


/*============================================================
8. FINDING & REMOVING DUPLICATES
============================================================*/

-- Find duplicate names
SELECT name, COUNT(*)
FROM employees
GROUP BY name
HAVING COUNT(*) > 1;

-- Delete duplicates (keeping minimum id)
DELETE FROM employees
WHERE id NOT IN (
    SELECT MIN(id)
    FROM employees
    GROUP BY name
);


/*============================================================
9. Nth HIGHEST SALARY (VERY COMMON QUESTION)
============================================================*/

-- 3rd highest salary using LIMIT (MySQL style)
SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 2;

-- Using DENSE_RANK
SELECT salary
FROM (
    SELECT salary,
           DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
    FROM employees
) t
WHERE rnk = 3;


/*============================================================
10. REAL-WORLD AUTOMATION TESTING SCENARIOS
============================================================*/

-- Verify user created in DB
SELECT *
FROM users
WHERE email = 'test@example.com';

-- Validate order status updated
SELECT status
FROM orders
WHERE order_id = 101;

-- Ensure record count increased
SELECT COUNT(*)
FROM orders;

-- Check if API inserted correct data
SELECT name, price
FROM products
WHERE product_id = 500;


/*============================================================
11. INDEXING (PERFORMANCE)
============================================================*/

-- Create index on salary
CREATE INDEX idx_salary
ON employees(salary);

-- Why?
-- Improves search speed on large tables
-- Important for performance-based interview questions


/*============================================================
12. TRANSACTIONS & ACID
============================================================*/

-- Start transaction
BEGIN;

UPDATE employees
SET salary = salary + 5000
WHERE id = 10;

-- Rollback if something wrong
ROLLBACK;

-- Commit if everything correct
COMMIT;


/*
============================================================
IMPORTANT THEORY FOR INTERVIEW
============================================================

ACID Properties:
A - Atomicity   (All or nothing)
C - Consistency (Valid state before & after)
I - Isolation   (Transactions don’t interfere)
D - Durability  (Data saved permanently)

Difference:
WHERE  -> Filters rows before grouping
HAVING -> Filters after GROUP BY

INNER JOIN -> Matching records only
LEFT JOIN  -> All left table records

ROW_NUMBER  -> Unique ranking
DENSE_RANK  -> Same rank for ties

============================================================
END OF FILE
============================================================
*/
