'''

Напишите регулярное выражение, которое найдёт все трёхбуквенные слова.
Что нужно найти:

Нужно найти последовательности, подходящие по следующим условиям:

    Состоит из 3 букв
    Используется латинский и кириллический алфавиты верхнего и нижнего регистров
    Окружена пробелами с двух сторон

Sample Input 1:

Значимость этих проблем настолько очевидна, что начало повседневной работы по формированию позиции требуют от нас анализа соответствующий условий активизации. Равным образом реализация намеченных плановых заданий позволяет оценить значение модели развития. Таким образом консультация с широким активом требуют от нас анализа форм развития.

Sample Output 1:

что   нас   нас

Sample Input 2:

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc aliquam felis ut nisl fermentum porttitor. Integer condimentum arcu eget maximus tincidunt. Ut interdum ligula nulla, non tempor arcu consequat in. Aliquam molestie est mauris, efficitur lacinia nisl dictum et. Donec sit amet justo eros. Etiam fermentum justo lectus, vitae tincidunt dolor lobortis sed. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

Sample Output 2:

sit   non   est   sit   sit

Sample Input 3:

The dog was wet. Now it is dry.

Sample Output 3:

dog   Now

Sample Input 4:

 эт0  _не  слова!

Sample Output 4:

Sample Input 5:

 чuЦ  СXI  хЦ[  цМф  D\М  зЗЩ  hNR  ulW  SШН  ЧZЙ  O1Л  у9D  ч7М  |э:  СcT  }9A  Лw?  Yц|  [_Z  IbБ  б ж  GRI  HУН  Йjп  <н_  *O2  oПP  ХgЗ  П$v  ;щ|  [М|  эGР  х^!  +пэ  ЬZ+  ЛЩЫ  iIX  0xР  KЧD  ёыW  О/g  ,CЪ  шБб  и]s  г^О  ^ТY  #х6  z@П  e-ш  Tяз  1tБ  GШz  \хБ  Tци  %ОЭ  5=b  пdО  тъы  Dw*  дПб  уrэ  ХФб  к|Ч  bix  bсщ  Щ\л  /Ё3  MЪZ  +и2  >kЁ  фЬH  #%=  ТОс  0Jз  х/А  D!Q  aA\  Z&П  ;Dg  ЖiД  bцa  jуa  G}о  g)Т  ?ЧQ  ~Гп  ?J"  {xН  нzь  Ш+ч  W\[  cХ7  кJ|  =хM  PKр  .fN  Иfт  <a?  5$U  Е(. 

Sample Output 5:

чuЦ   СXI   цМф   зЗЩ   hNR   ulW   SШН   ЧZЙ   СcT   IbБ   GRI   HУН   Йjп   oПP   ХgЗ   эGР   ЛЩЫ   iIX   KЧD   ёыW   шБб   Tяз   GШz   Tци   пdО   тъы   дПб   уrэ   ХФб   bix   bсщ   MЪZ   фЬH   ТОс   ЖiД   bцa   jуa   нzь   PKр   Иfт

Sample Input 6:

في هذه المهمة ، نبحث فقط عن الكلمات ذات الأحرف اللاتينية أو السيريلية.

Sample Output 6:

'''

regex = r' [A-Za-zа-яА-яёЁ]{3} '
