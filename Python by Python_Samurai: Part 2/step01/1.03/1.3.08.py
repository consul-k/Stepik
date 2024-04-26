a = input().split()
new_lst = []
for word in a:
    if len(word) > 5:
        new_lst.append(len(word))
    else:
        new_lst.append(word)
print(new_lst)
