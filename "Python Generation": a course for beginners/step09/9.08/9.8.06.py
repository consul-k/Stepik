n = int(input())

books = []
for _ in range(n):
    book = input()
    books.append(book)

is_sorted = True

for i in range(1, n):
    prev_author = books[i-1].split(' ')[0]
    curr_author = books[i].split(' ')[0]
    
    if curr_author < prev_author:
        is_sorted = False
        break
    elif curr_author == prev_author:
        prev_title_start = books[i-1].find('«') + 1
        prev_title_end = books[i-1].find('»')
        prev_title = books[i-1][prev_title_start:prev_title_end]
        
        curr_title_start = books[i].find('«') + 1
        curr_title_end = books[i].find('»')
        curr_title = books[i][curr_title_start:curr_title_end]
        
        if curr_title < prev_title:
            is_sorted = False
            break

print("YES" if is_sorted else "NO")
