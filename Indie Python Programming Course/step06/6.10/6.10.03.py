'''

В наши дни очень много парней ставят себе фотографии красивых девушек на аватарки на форумах. 
Из-за этого очень часто сложно определить пол пользователя на форуме. В прошлом году наш герой пообщался в чате на форуме с одной красоткой (как он думал). 
После этого наш герой и предполагаемая красотка стали общаться еще чаще и в конце концов стали парой в сети.

Но вчера наш герой захотел увидеть свою красотку в реальной жизни и, каково же было его удивление, когда красоткой оказался здоровенный мужчина! 
Наш герой очень расстроился и теперь он, наверное, никогда больше не сможет полюбить. 
Сейчас к нему пришла в голову идея, как по имени пользователя определить его пол.

Вот его метод: если количество различных символов в имени пользователя нечетное, тогда пользователь мужского пола, иначе — женского. 
Вам дана строка, обозначающая имя пользователя, помогите нашему герою определить по ней пол пользователя по описанному методу.
Входные данные

В первой строке записана непустая строка, состоящая только из строчных букв латинского алфавита — имя пользователя. 
Эта строка состоит из не более чем 100 букв.
Выходные данные

Если пользователь оказался женского пола по методу нашего героя, выведите «CHAT WITH HER!» (без кавычек), иначе, выведите «IGNORE HIM!» (без кавычек).

Sample Input 1:

abra

Sample Output 1:

IGNORE HIM!

Sample Input 2:

sevenkplus

Sample Output 2:

CHAT WITH HER!

'''

a = set(input())
if len(a)%2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')
