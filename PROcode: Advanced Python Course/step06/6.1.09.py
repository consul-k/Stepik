symbols = input().split()

symbols_tuple = tuple(symbols)

letters = [char for char in symbols_tuple if char.isalpha()]

message = ''.join(letters)

length = len(message)
if length == 0:
    key_letter = ""
elif length % 2 == 1:
    # Нечетное количество букв - берем центральную
    key_letter = message[length // 2]
else:
    # Четное количество букв - берем правую от центра
    key_letter = message[length // 2]

print(message)
print(f"Ключевая буква: {key_letter}")
