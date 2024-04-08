SELECT oms_num, SUM(visit_amount) AS sum_visit
FROM talons
GROUP BY oms_num;
