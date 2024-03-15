user_input = int(input(""))
l = []

while user_input != 0:
    l.append(user_input)
    user_input = int(input())
    
print(f'Сумма всех введенных чисел: {sum(l)}')
