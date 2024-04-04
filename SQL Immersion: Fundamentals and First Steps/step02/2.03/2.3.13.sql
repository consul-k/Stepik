SELECT *
FROM Orders
WHERE order_sum > 500 AND NOT status = 'Доставлен';
