SELECT full_name, oms_num, YEAR(CURDATE()) - YEAR(birth_date) AS age
FROM patients;
