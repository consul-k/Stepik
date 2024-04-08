SELECT spec, COUNT(doctor_num) AS count_docs
FROM doctors
GROUP BY spec;
