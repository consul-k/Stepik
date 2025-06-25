# Читаем имя файла из ввода
filename = input().strip()

# далее ваш код
file = open(filename, 'r')
content = file.read()
print(content)
file.close()

file = open(filename, 'r')
line = file.readline()
print(line)
file.close()
