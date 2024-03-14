num1 = 235
num2 = 18

str1 = "Программирование"
str2 = "Python"

a = str(num1) + str1[:3]
b = str(num2) + str2[-4:]
s = a + ' ' + b

print(f"Итоговая строка: {s}")
print(f"Последовательность \'23\' встречается {s.count('23')} раз.")
print(f"Произведение длины строки на num2: {len(s)*num2}")
