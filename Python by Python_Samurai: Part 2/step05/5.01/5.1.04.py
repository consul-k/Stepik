def func(word):
    s = 0
    for i in word:
        if i.isdigit():
            s += int(i)
    print(s)
