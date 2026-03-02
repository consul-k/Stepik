count_messages = 0
count_long_messages = 0

while True:
    message = input()
    count_messages += 1
    
    if len(message) > 7:
        count_long_messages += 1
    
    if message[-2:] == '11':
        break

print(f"{count_long_messages}/{count_messages}")
