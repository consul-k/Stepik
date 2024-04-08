CREATE TABLE books_in_use
(
    reader_num INT,
    book_num INT,
    issue_date DATE,
    return_date DATE,
    return_period TINYINT NOT NULL DEFAULT 14,
    fine_amount DECIMAL(10,2) NOT NULL DEFAULT 0,
    PRIMARY KEY(reader_num, book_num, issue_date),
    FOREIGN KEY (reader_num) REFERENCES readers(reader_num),
    FOREIGN KEY (book_num) REFERENCES books(book_num)
);
