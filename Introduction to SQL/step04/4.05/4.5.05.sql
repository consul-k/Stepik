SELECT doctor_num
FROM talons
GROUP BY doctor_num
HAVING COUNT(oms_num) > 1;
