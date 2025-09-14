import sys

rus_lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
rus_upper = rus_lower.upper()
lat_lower = "abcdefghijklmnopqrstuvwxyz"
lat_upper = lat_lower.upper()

trans = {}
for s in (rus_lower, rus_upper, lat_lower, lat_upper):
    for i, ch in enumerate(s):
        trans[ch] = s[(i + 1) % len(s)]

data = sys.stdin.read()
out = []
for ch in data:
    out.append(trans.get(ch, ch))

sys.stdout.write("".join(out))
