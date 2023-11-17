'''

Создайте список первых букв каждого слова из строки st и выведите его на экран

'''

st = 'Create a list of the first letters of every word in this string'
s = [i[0] for i in st.split()]
print(s)
