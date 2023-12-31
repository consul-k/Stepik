'''

Найдите все слова да, нет, наверное в тексте. Они могут начинаться с букв разных регистров.
Что нужно найти:

Нужно найти последовательности, подходящие по следующим условиям:

    Это последовательность да, нет, наверное
    Не является подпоследовательностью

Sample Input 1:

«Да нет наверное» - фраза непонятная многим иностранцам. Это означает как бы "нет", только с сомнением "а вдруг?!"

Sample Output 1:

Да нет наверное нет

Sample Input 2:

Запятая между союзами что и когда есть только в том предложении, где нет слова тогда.

Sample Output 2:

нет

Sample Input 3:

Да да Нет нет Наверное наверное дар когда

Sample Output 3:

Да да Нет нет Наверное наверное

Sample Input 4:

Множество планет. Звон монет

Sample Output 4:

'''

regex = r'\b(?:[Дд]а|[Нн]ет|[Нн]аверное)\b'
