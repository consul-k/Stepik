n = int(input())
s = {}
for i in range(1,n+1):
    if (a := input()) not in s:
        print('OK')
        s[a] = 1
    else:
        print(a + str(s[a]))
        s[a] = s[a] + 1
