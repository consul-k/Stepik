'''

Напишите регулярное выражение, которое найдёт все переменные, записанные в стиле snake_case.
Что нужно найти:

Как вы уже поняли - snake_case это тоже стиль наименования переменных. В Python переменные принято называть, используя этот стиль. Вот что он из себя представляет:

    Всегда используется нижний регистр
    Слова разделяются нижним подчёркиванием
    Используются буквы латинского алфавита
    Цифры в переменных из тестовых данных находятся только в конце.

Примеры использования:

    variable
    quite_long_variable
    two_words

Sample Input 1:

get_id sendMessage echo_all canvas wrapper RegularExpression upperCAse nice_Flick_SHOT that_was_bad 

Sample Output 1:

get_id echo_all canvas wrapper that_was_bad

Sample Input 2:

project_one project_1 test_2 test_3 test_4 variable_5 var_6 var_7 var_8 var_9 var_42342354325

Sample Output 2:

project_one project_1 test_2 test_3 test_4 variable_5 var_6 var_7 var_8 var_9 var_42342354325

Sample Input 3:

just_a_variable Wrong_Variable SendNudes doubleShibaInu 

Sample Output 3:

just_a_variable

'''
