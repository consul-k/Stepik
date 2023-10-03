'''

Вы снова получили доступ к информации, которая предназначена не для вас. Прошёл слух, что на хостинге изображений imgur хранятся пароли от криптокошелька. Вы собираетесь прошерстить всё, что у вас есть, и найти все ссылки на этот хостинг. Каждая ссылка должна быть на новой строке.
Что нужно сделать:

Нужно найти последовательности, подходящие по следующим условиям:

    Начинается с https://imgur.com/
    Потом идёт 7 симолов из следующего диапазона: a-z, A-Z, 0-9

Тестовые данные:
Входные данные:

На вход программе подаётся 1 строка.
Выходные данные:

Ваша задача вывести все ссылки в тексте.

Sample Input 1:

У лукоморья дуб зелёный;Златая цепь на дубе том:И днём и ночью кот учёныйВсё ходит по цепи кругом;Идёт на https://weboas.is/право — песнь заводит,Налево — сказку говорит.Там чудеса: там леший бродит,Русалка на ветвях сидит;Там на неведомых дорожкахСледы невиданных зверей;Избушка там на курьих ножкахСтоитhttps://www.youtube.com/без окон, без дверей;Т https://imgur.com/pecSvGKам лес и дол видений полны;Там о заре прихлынут волныНа брег песчаный и пустой,И тридцать витязей прекрасныхЧредой из вод выходят ясных,И с ними дядька их морской;Там королевич мимоходомПленяет грозного царя;Там в облаках перед народом https://imgur.com/LHbcwKWЧерез леса, через моряКолдун несёт богатыря;В темнице там царевна тужит,А бурый волк ей верно служит;Там ступа с Бабою ЯгойИдёт, бредёт https://imgur.com/xM6Pc8R сама собой,Там царь Кащей над златом чахнет;Там русский дух… там Русью пахнет!И там яhttps://imgur.com/nD6OEUXбыл, и мёд я пил;У моря видел дуб зелёный;Под ним сидел, и кот учёныйСвои мне сказки говорил.

Sample Output 1:

https://imgur.com/pecSvGK
https://imgur.com/LHbcwKW
https://imgur.com/xM6Pc8R
https://imgur.com/nD6OEUX

Sample Input 2:

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry'https://imgur.com/hpjus8ds standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scramblhttps://imgur.com/y2lgyvYed it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, rehttps://imgur.com/jJb53h2maining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passhttps://imgur.com/xYy6hjAages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsumhttps://imgur.com/oaUzSly.

Sample Output 2:

https://imgur.com/hpjus8d
https://imgur.com/y2lgyvY
https://imgur.com/jJb53h2
https://imgur.com/xYy6hjA
https://imgur.com/oaUzSly

Sample Input 3:

The standardhttps://imgur.com/8oHc67r Lorem Ipsumhttps://imgur.com/3rGUJqOpassage, used since the 1500s

Sample Output 3:

https://imgur.com/8oHc67r
https://imgur.com/3rGUJqO

'''

import re

result = re.findall(r'https://imgur.com/[a-zA-Z0-9]{7}', input())
for i in result:
    print(i)
