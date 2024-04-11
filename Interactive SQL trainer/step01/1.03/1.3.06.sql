select round(avg(price),2) as Средняя_цена, sum(price*amount) as Стоимость
from book
where amount between 5 and 14
