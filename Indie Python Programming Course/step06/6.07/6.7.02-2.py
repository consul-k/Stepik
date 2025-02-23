filtered_books = {key: value for key, value in books.items() if len(key) % 3 == 0}

print(filtered_books)
