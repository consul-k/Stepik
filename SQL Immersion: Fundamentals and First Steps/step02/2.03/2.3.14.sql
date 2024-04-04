SELECT *
FROM Employees
WHERE (department = 'Marketing' OR department = 'Sales') AND NOT on_vacation = 1;
