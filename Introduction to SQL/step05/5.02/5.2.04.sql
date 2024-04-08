UPDATE books_in_use
SET fine_amount = IF(DATEDIFF(return_date, issue_date) > return_period,  DATEDIFF(return_date, issue_date) - return_period, 0) * 8.45
WHERE return_date IS NOT NULL;
