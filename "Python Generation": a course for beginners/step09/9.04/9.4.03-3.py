n = int(input())
count_odi_messages = 0

for _ in range(n):
    message = input()
    count_11 = 0
    i = 0
    while i < len(message) - 1:
        if message[i] == '1' and message[i + 1] == '1':
            count_11 += 1
            i += 2
        else:
            i += 1
    if count_11 >= 3:
        count_odi_messages += 1

print(count_odi_messages)
