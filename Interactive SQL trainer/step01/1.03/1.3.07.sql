SELECT author, SUM(price * amount) AS Стоимость
FROM book
WHERE title NOT IN ("Идиот", "Белая гвардия")
GROUP BY author
HAVING SUM(price * amount) > 5000
ORDER BY Стоимость DESC;
