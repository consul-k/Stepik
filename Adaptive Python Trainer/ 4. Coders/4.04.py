k = int(input())
text = input()

BASE = 0x1F600
END = 0x1F64F
N = END - BASE + 1
res = []
for ch in text:
    c = ord(ch)
    if BASE <= c <= END:
        res.append(chr(BASE + (c - BASE + k) % N))
    else:
        res.append(ch)

print(f'Result: "{"".join(res)}"')
