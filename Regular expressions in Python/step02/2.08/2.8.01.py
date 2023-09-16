'''

Напишите регулярное выражение, которое найдёт все use strict; и use strict в тексте.

Что нужно найти:

Последовательности use strict; и use strict

Sample Input 1:

someSpamuuse stricttещёспам

Sample Output 1:

use strict

Sample Input 2:

strict;use strict;use

Sample Output 2:

use strict;

Sample Input 3:

strict;use strict;;;;;use

Sample Output 3:

use strict;

Sample Input 4:

use strict< use strict= use strict> use strict? use strict@ use strictA use strictB use strictC use strictD use strictE use strictF use strictG use strictH use strictI use strictJ use strictK use strictL use strictM use strictN use strictO use strictP use strictQ use strictR use strictS use strictT use strictU use strictV use strictW use strictX use strictY use strictZ use strict[ use strict] use strict^ use strict_ use strict` use stricta use strictb use strictc use strictd use stricte use strictf use strictg use stricth use stricti use strictj use strictk use strictl use strictm use strictn use stricto use strictp use strictq use strictr use stricts use strictt use strictu use strictv use strictw use strictx use stricty use strictz use strict{ use strict| use strict} use strict~ use strictа use strictб use strictв use strictг use strictд use strictе use strictё use strictж use strictз use strictи use strictй use strictк use strictл use strictм use strictн use strictо use strictп use strictр use strictс use strictт use strictу use strictф use strictх use strictц use strictч use strictш use strictщ use strictъ use strictы use strictь use strictэ use strictю use strictя use strictА use strictБ use strictВ use strictГ use strictД use strictЕ use strictЁ use strictЖ use strictЗ use strictИ use strictЙ use strictК use strictЛ use strictМ use strictН use strictО use strictП use strictР use strictС use strictТ use strictУ use strictФ use strictХ use strictЦ use strictЧ use strictШ use strictЩ use strictЪ use strictЫ use strictЬ use strictЭ use strictЮ use strictЯ use strict  use strict! use strict" use strict# use strict$ use strict% use strict& use strict\ use strict' use strict( use strict) use strict* use strict+ use strict, use strict- use strict. use strict/ use strict0 use strict1 use strict2 use strict3 use strict4 use strict5 use strict6 use strict7 use strict8 use strict9 use strict: use strict; 

Sample Output 4:

use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict use strict;

Sample Input 5:

use str1ct Use strict uuu strict три буквыы USE STRICT

Sample Output 5: 

'''

regex = r'use strict;?'
