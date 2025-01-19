word = input()
if word == 'Вселенная':
    answer = 'Поздравляю, это правильный ответ!'

try:   
    print(answer)
except NameError:
    print('Неправильный ответ')
