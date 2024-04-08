SELECT sex, COUNT(sex) AS count_pacient
FROM patients
WHERE YEAR(birth_date) > 1970
GROUP BY sex;
