SELECT order_id, amount AS TotalAmount, date
FROM Orders
WHERE amount > 1000 AND amount < 5000
ORDER BY amount DESC;
