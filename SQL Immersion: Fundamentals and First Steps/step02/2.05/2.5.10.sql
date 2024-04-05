SELECT name AS EmployeeName, department, age AS Age
FROM Employees
WHERE years_of_experience > 5
ORDER BY department, age DESC;
