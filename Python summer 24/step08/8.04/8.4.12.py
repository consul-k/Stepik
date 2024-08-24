m = int(input())
n = int(input())
books = set()
lib = []

for book in range(m):
    book = input()
    books.add(book)
    
for lib_book in range(n):
    lib_book = input()
    lib.append(lib_book)
    
for check in lib:
    if check in books:
        print('YES')
    else:
        print('NO')
