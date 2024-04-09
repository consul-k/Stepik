SELECT book_author, COUNT(book_name) AS books_count
FROM books
WHERE book_author in ('Чехов', 'Тургенев')
GROUP BY book_author;
