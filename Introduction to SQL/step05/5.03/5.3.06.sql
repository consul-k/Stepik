SELECT MIN(fine_amount) AS min_fine_amount
FROM books_in_use
WHERE fine_amount > 0;
