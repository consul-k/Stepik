n = int(input())

books = []
for _ in range(n):
    books.append(input())

filtered_books = filter(lambda book: int(book.split()[-1]) > 2000, books)

book_titles = [book.rsplit(' ', 1)[0] for book in filtered_books]

print("Книги, выпущенные после 2000 года:")
print(book_titles)
