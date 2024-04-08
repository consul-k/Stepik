CREATE TABLE books
(
    book_num INT AUTO_INCREMENT,
    book_author VARCHAR(100),
    book_name VARCHAR(100),
    book_count TINYINT NOT NULL DEFAULT 0,
    PRIMARY KEY(book_num)
);
