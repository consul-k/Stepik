str1 = "Программирование"
str2 = "Python"
str3 = "Забавно!"
a = ''

a += str1[4:11]
a += str2[:3]
a += str3[-4:]
a = a.capitalize()

print(f"Итоговая строка: {a}")
print(f"Буква \'о\' встречается {a.lower().count('о')} раз.")
