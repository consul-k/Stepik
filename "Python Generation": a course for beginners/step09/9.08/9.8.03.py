s1 = input().strip()
s2 = input().strip()

letters1 = ''.join(ch.lower() for ch in s1 if ch.isalpha())
letters2 = ''.join(ch.lower() for ch in s2 if ch.isalpha())

if letters1 == letters2:
    print("YES")
else:
    print("NO")
