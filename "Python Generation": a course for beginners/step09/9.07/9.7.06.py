eng_chars = "eyopaxcETOPAHXCBM"
rus_chars = "еуорахсЕТОРАНХСВМ"

replace_map = {}
for e, r in zip(eng_chars, rus_chars):
    replace_map[e] = r

text = input()

old_cost = 0
for ch in text:
    old_cost += ord(ch) * 3

new_cost = 0
for ch in text:
    new_ch = replace_map.get(ch, ch)
    new_cost += ord(new_ch) * 3

print(f"Старая стоимость: {old_cost}🐝")
print(f"Новая стоимость: {new_cost}🐝")
