SELECT *
FROM Customers
WHERE (city = 'New York' OR city = 'Los Angeles') AND NOT loyalty_member = 1;
