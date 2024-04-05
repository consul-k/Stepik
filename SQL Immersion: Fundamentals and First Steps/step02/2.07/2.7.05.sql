SELECT *
FROM Customers
WHERE city in ('Москва', 'Санкт-Петербург') AND (name LIKE 'А%' or name LIKE 'Б%');
