'''

Напишите программу, которая будет заменять символы строки на другую раскладку клавиатуры. Программа должна работать в обе стороны.

Ввод:

Строка s, состоящая из символов. В случае русской раскладки – на вход идут только буквы в нижнем регистре, 
в обратном случае – их эквиваленты на клавише клавиатуры.

Вывод:

Строка в другой раскладке клавиатуры

Sample Input 1:

йцукен

Sample Output 1:

qwerty

Sample Input 2:

qwerty

Sample Output 2:

йцукен

Sample Input 3:

asdfghj

Sample Output 3:

фывапро

'''

word = input()
trans_word = ''

rus_to_eng = {'й': 'q', 'ц': 'w', 'у': 'e', 'к': 'r', 'е': 't', 'н': 'y', 'г': 'u', 'ш': 'i', 'щ': 'o', 'з': 'p', 'х': '[', 'ъ': ']', 'ф': 'a', 'ы': 's', 'в': 'd', 'а': 'f', 'п': 'g', 'р': 'h', 'о': 'j', 'л': 'k', 'д': 'l', 'ж': ';', 'э': "'", 'я': 'z', 'ч': 'x', 'с': 'c', 'м': 'v', 'и': 'b', 'т': 'n', 'ь': 'm', 'б': ',', 'ю': '.', 'ё': '`'}

eng_to_rus = {v: k for k, v in rus_to_eng.items()}

if word[0] in rus_to_eng:
    for l in word:
        trans_word += rus_to_eng[l]
    print(trans_word)
else:
    for l in word:
        trans_word += eng_to_rus[l]
    print(trans_word)
