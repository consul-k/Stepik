cnt = 1
for i in sorted(list_num, reverse=True):
    if cnt <= 4:
        print(i, end=' ')
        cnt += 1
