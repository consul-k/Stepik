SELECT *
FROM Products
WHERE (category = 'Electronics' OR category = 'Clothing') AND price > 100 AND on_sale = 0;
