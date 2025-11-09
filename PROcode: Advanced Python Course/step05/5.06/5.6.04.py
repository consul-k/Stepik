old_books = (
    'Мастер и Маргарита',
    'Война и мир',
    '1984',
    'Преступление и наказание',
    '451 градус по Фаренгейту',
    '1984'
)

print(f"Исходный кортеж книг: {old_books}")

new_books_input = input().strip()
new_books_list = [book.strip() for book in new_books_input.split(',')]

all_books = list(old_books) + new_books_list

unique_books = []
for book in all_books:
    if book not in unique_books:
        unique_books.append(book)

sorted_books = sorted(unique_books)

new_books_tuple = tuple(sorted_books)
print(f"Новый кортеж книг: {new_books_tuple}")
