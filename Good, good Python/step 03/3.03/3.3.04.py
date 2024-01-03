'''

Подвиг 7. Вводится строка (слаг). Замените в этой строке все двойные дефисы (--) и тройные (---) на одинарные (-). 
Подумайте, в какой последовательности следует выполнять эти замены. Результат преобразования выведите на экран.

Sample Input:

dobavlyaem---slagi--slug-k--url---adresam

Sample Output:

dobavlyaem-slagi-slug-k-url-adresam

'''

s = input()
print(s.replace('---','-').replace('--','-'))
