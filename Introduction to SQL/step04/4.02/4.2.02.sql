SELECT DOCTOR_NUM, DOCTOR_NAME, IF(ISNULL(SPEC), 'Не заполнена', SPEC) as SPEC
FROM doctors;
