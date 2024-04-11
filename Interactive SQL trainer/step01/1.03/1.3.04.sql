SELECT author, ROUND(SUM(price*amount),2) AS Стоимость,
        ROUND(SUM(price*amount)*(18/100)/(1+(18/100)),2) AS НДС,
        ROUND(SUM((price*amount)/(1+(18/100))),2) AS Стоимость_без_НДС 
FROM book
GROUP BY author;
