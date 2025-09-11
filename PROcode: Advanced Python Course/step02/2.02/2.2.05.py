desyatikom_num, polovinnik_num = map(float, input().split())

desyatikom_result = desyatikom_num * 2
polovinnik_result = polovinnik_num / 2

# Сравниваем результаты и выводим победителя
if desyatikom_result > polovinnik_result:
    print("Победил Десятиком!")
elif desyatikom_result < polovinnik_result:
    print("Победил Половинник!")
else:
    print("Ничья! Числа равны.")
