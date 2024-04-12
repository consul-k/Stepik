SELECT author,title,price, ROUND((SELECT AVG(price) FROM book),2) AS Средняя_цена
FROM book
WHERE price BETWEEN ((SELECT AVG(price) FROM book)-70) AND ((SELECT AVG(price) FROM book)+70);
