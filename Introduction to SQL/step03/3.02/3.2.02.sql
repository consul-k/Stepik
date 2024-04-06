UPDATE med_area
SET area_address = CONCAT('г. Москва, ', area_address)
WHERE area_num;
