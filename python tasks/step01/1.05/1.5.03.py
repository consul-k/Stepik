f_word = input()
s_word = input()

if f_word[0] in s_word:
    print(s_word.index(f_word[0]))
else:
    print(-1)
