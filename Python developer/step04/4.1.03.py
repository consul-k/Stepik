'''

Напишите программу, которая получает на вход две строки – логин и пароль пользователя. Определите верная ли это комбинация используя следующие условия:

    длина логина должна быть > 4;
    длина пароля должна быть > 8;
    логин не должен быть равен паролю.

В качестве результата работы программы выведите True или False.

Sample Input 1:

login
password1

Sample Output 1:

True

Sample Input 2:

1
1

Sample Output 2:

False

Sample Input 3:

password1
password1

Sample Output 3:

False

Sample Input 4:

1
2

Sample Output 4:

False

'''

login, password = input(), input()
print(len(login)>4 and len(password)>8 and login != password)
