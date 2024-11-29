word = input()
n = int(input())

if len(word) == n:
    print("=")
elif len(word) > n:
    print(">")
else:
    print("<")
