'''

Вводится целое число, необходимо выполнить выравнивание его по центру, отведя 15 символов под отображение числа. 
Символом заполнителем должен являться знак дефиса -

Sample Input 1:

17

Sample Output 1:

------17-------

Sample Input 2:

123456789

Sample Output 2:

---123456789---   

'''

print(f'{int(input()):-^15}')
