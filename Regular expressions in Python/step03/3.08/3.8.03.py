'''

Разделите текст по категориям, тем самым получив товары из каждой категории.
Что нужно сделать:

Нужно найти последовательности, подходящие по следующим условиям:

    Начинается с Категория: 
    Потом идёт последовательность из кириллических символов обоих регистров и пробелов
    Минимальная длина последовательности 1 символ
    Заканчивается на \n

Тестовые данные:
Входные данные:

На вход программе подаётся 1 строка.
Выходные данные:

Ваша задача вывести полученный список всех товары, разделённых по категориям.

Sample Input 1:

Категория: Телефоны\nSupreme Burner\nMotorola Razr\nКатегория: Смарт часы и браслеты\nApple Watch 6\nGarmin Venu\nXiaomi Mi Smart Band 6\nКатегория: Игры\nSpore

Sample Output 1:

['', 'Supreme Burner\\nMotorola Razr\\n', 'Apple Watch 6\\nGarmin Venu\\nXiaomi Mi Smart Band 6\\n', 'Spore']

Sample Input 2:

Категория: Персональные компьютеры\nDEXP Mars E326\nMSI MAG Codex 5 11SC-670XRU\nZET Gaming WARD H125\nКатегория: Ноутбуки\nMSI GE76 11UH-261RU\nLenovo Legion 7 16ITHg6\nApple MacBook Pro Z14V0008E\nMSI GS76 11UH-265RU\nMSI GS66 Stealth 11UH-252RU\nMSI GS66 11UH-263RU\nКатегория: Моноблоки\nHP 32-a1006ur\nApple iMac

Sample Output 2:

['', 'DEXP Mars E326\\nMSI MAG Codex 5 11SC-670XRU\\nZET Gaming WARD H125\\n', 'MSI GE76 11UH-261RU\\nLenovo Legion 7 16ITHg6\\nApple MacBook Pro Z14V0008E\\nMSI GS76 11UH-265RU\\nMSI GS66 Stealth 11UH-252RU\\nMSI GS66 11UH-263RU\\n', 'HP 32-a1006ur\\nApple iMac']

'''

import re

result = re.split(r'Категория: [а-яА-ЯёЁ ]+\\n', input())
print(result)
