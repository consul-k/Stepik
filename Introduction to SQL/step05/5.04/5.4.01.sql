SELECT book_author, COUNT(book_name) AS books_count
FROM books
GROUP BY book_author;
