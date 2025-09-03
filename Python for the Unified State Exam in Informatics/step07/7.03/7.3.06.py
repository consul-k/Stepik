books = input().split()
search = input()

if search in books:
    print(books.index(search))
else:
    print(-1)
