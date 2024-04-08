SELECT sex, COUNT(sex) AS count_pacient
FROM patients
GROUP BY sex;
