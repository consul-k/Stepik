SELECT book_id AS Порядковый_номер, author AS Автор, ROUND(AVG(price)) AS Средняя_цена 
FROM book
GROUP BY book_id, author
HAVING Порядковый_номер > 2;
