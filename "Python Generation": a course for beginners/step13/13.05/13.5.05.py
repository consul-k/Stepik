# объявление функции
def is_one_away(word1, word2):
    if len(word1) == len(word2):
        dif = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                dif += 1
        return dif == 1
    return False

# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))
