alphabet = ' abcdefghijklmnopqrstuvwxyz'
n = len(alphabet)

k = int(input().strip())
s = input().strip()

k %= n
index = {c: i for i, c in enumerate(alphabet)}

res = ''.join(alphabet[(index[ch] + k) % n] for ch in s)

print(f'Result: "{res}"')
