nickname = input().strip()

if (nickname.startswith('@') and
    5 <= len(nickname) <= 15 and
    all('a' <= c <= 'z' or '0' <= c <= '9' for c in nickname[1:])):
    print("Correct")
else:
    print("Incorrect")
