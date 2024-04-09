SELECT book_author
FROM books
GROUP BY book_author
HAVING COUNT(book_name) = 1;
