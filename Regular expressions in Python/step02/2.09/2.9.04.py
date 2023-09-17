'''

Напишите регулярное выражение, которое найдёт минимальную последовательность, начинающуюся на букву и заканчивающуюся буквой.
Что нужно найти:

Нужно найти последовательности, подходящие по следующим условиям:

    Начинается и заканчивается буквой
    Используются буквы из латинского и кириллического алфавитов верхнего и нижнего регистров
    Между буквами могут находиться последовательности из любых символов
    Длина последовательности должна быть минимально возможной

Sample Input 1:

RFB 9W90rb9-4br9-wB9-DFWHE9R980br8wr vh9f n0iwoedo-wqk-0oen239rn0-3n0d3w2eb9erdbn3

Sample Output 1:

RF B 9W rb br wB DF WH E9R br wr vh f n iw oe do wq k-0o en rn n0d w2e b9e rd bn

Sample Input 2:

аpM+m.tnDсм&ВksWУюзАЪlqе|гa?Ш=S9хzСцrХ4vc2ЦК':g^к`Щ6%б]{#yОЫГТшйЕБ0iЬfEжGAПjXыU)VЧтYF}дв_KИ[5>лOэLHbЯЖЮxЁ\ъ8!,рoо"hQЛu;щч7<РNTP@eНЗп1ДнBФё$я/ьdуЭ(М-3фR*~ JиZwЙCI

Sample Output 2:

аp M+m tn Dс м&В ks WУ юз АЪ lq е|г a?Ш S9х zС цr Х4v c2Ц К':g к`Щ б]{#y ОЫ ГТ шй ЕБ iЬ fE жG AП jX ыU VЧ тY F}д в_K И[5>л Oэ LH bЯ ЖЮ xЁ ъ8!,р oо hQ Лu щч РN TP eН Зп Дн BФ ё$я ьd уЭ М-3ф R*~ J иZ wЙ CI

Sample Input 3:

ABCDEF64G6JRWS

Sample Output 3:

AB CD EF G6J RW

'''

regex = r'[a-zA-Zа-яА-ЯЁё].*?[a-zA-Zа-яА-ЯЁё]'
