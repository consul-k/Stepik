SELECT product_id, SUM(quantity) AS total_quantity, SUM(total_price) AS total_sales
FROM Sales 
GROUP BY product_id
ORDER BY total_quantity DESC
LIMIT 5;
