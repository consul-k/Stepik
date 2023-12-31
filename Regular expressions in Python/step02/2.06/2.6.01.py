'''

Напишите регулярное выражение, которое найдет все последовательности: сон, сок, сом.

Что нужно найти:

Последовательности: сон, сок, сом.

Sample Input 1:

Пью сок вместе с моим сомом.

Sample Output 1:

сок сом

Sample Input 2:

Ты прервал мой сон!

Sample Output 2:

сон

Sample Input 3:

сом сок сон

Sample Output 3:

сом сок сон

Sample Input 4:

со< со= со> со? со@ соA соB соC соD соE соF соG соH соI соJ соK соL соM соN соO соP соQ соR соS соT соU соV соW соX соY соZ со[ со] со^ со_ со` соa соb соc соd соe соf соg соh соi соj соk соl соm соn соo соp соq соr соs соt соu соv соw соx соy соz со{ со| со} со~ соа соб сов сог сод сое соё сож соз сои сой сок сол сом сон соо соп сор сос сот соу соф сох соц соч сош сощ соъ соы соь соэ сою соя соА соБ соВ соГ соД соЕ соЁ соЖ соЗ соИ соЙ соК соЛ соМ соН соО соП соР соС соТ соУ соФ соХ соЦ соЧ соШ соЩ соЪ соЫ соЬ соЭ соЮ соЯ со  со! со" со# со$ со% со& со\ со' со( со) со* со+ со, со- со. со/ со0 со1 со2 со3 со4 со5 со6 со7 со8 со9 со: со; СОМ СОК СОН сОн Сон соН СоН сОН СОн нос сно ско скн снк нкс оск осн

Sample Output 4:

сок сом сон

'''

regex = r'со[нкм]'
