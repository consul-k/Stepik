SELECT SUM(visit_amount) AS sum_amount_2023
FROM talons
WHERE YEAR(visit_time) = 2023;
