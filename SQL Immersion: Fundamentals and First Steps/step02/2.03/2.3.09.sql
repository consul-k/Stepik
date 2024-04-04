SELECT *
FROM Employees
WHERE (department = 'HR' or department = 'Sales') and years_of_experience > 3;
