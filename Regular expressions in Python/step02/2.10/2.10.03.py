'''
Напишите регулярное выражение, которое найдёт все повторяющиеся буквы в тексте.
Что нужно найти:

Нужно найти последовательности, подходящие по следующим условиям:

    Последовательность из 2 одинаковых букв
    Используются буквы латинского и кириллического алфавитов нижнего и верхнего регистров

Sample Input 1:

gg wp

Sample Output 1:

gg

Sample Input 2:

Сломанная лиственница и гостиная, украшенная стеклянными вазами. 

Sample Output 2:

нн нн нн нн

Sample Input 3:

carefully, AGREE, bill, сobble

Sample Output 3:

ll EE ll bb

Sample Input 4:

<<==>>??@@AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ[[]]^^__``aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz{{||}}~~ааббввггддееёёжжззииййккллммннооппррссттууффххццччшшщщъъыыььээююяяААББВВГГДДЕЕЁЁЖЖЗЗИИЙЙККЛЛММННООППРРССТТУУФФХХЦЦЧЧШШЩЩЪЪЫЫЬЬЭЭЮЮЯЯ  !!""##$$%%&&\\''(())**++,,--..//00112233445566778899::;;

Sample Output 4:

AA BB CC DD EE FF GG HH II JJ KK LL MM NN OO PP QQ RR SS TT UU VV WW XX YY ZZ aa bb cc dd ee ff gg hh ii jj kk ll mm nn oo pp qq rr ss tt uu vv ww xx yy zz аа бб вв гг дд ее ёё жж зз ии йй кк лл мм нн оо пп рр сс тт уу фф хх цц чч шш щщ ъъ ыы ьь ээ юю яя АА ББ ВВ ГГ ДД ЕЕ ЁЁ ЖЖ ЗЗ ИИ ЙЙ КК ЛЛ ММ НН ОО ПП РР СС ТТ УУ ФФ ХХ ЦЦ ЧЧ ШШ ЩЩ ЪЪ ЫЫ ЬЬ ЭЭ ЮЮ ЯЯ

'''

regex = r'([A-Za-zА-Яа-яёЁ]{1})\1'
