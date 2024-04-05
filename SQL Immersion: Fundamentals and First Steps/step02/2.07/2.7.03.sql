SELECT *
FROM Employees
WHERE department in ('HR', 'Marketing')
ORDER BY age DESC
LIMIT 5;
