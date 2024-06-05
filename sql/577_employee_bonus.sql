-- Write your PostgreSQL query statement below
SELECT e.name, b.bonus
FROM employee AS e
LEFT JOIN bonus AS b
ON e.empId = b.empId
WHERE b.bonus < 1000 OR b.bonus IS null
