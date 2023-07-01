/*


Используя символы табуляции, измените вызов функции printf так, чтобы получалась красивая табличка. Учтите, что позиции табуляции у вас и в проверяющей системе могут иметь различные значения.

P.S. В программе используются некоторые конструкции, которые вы пока не знаете. Не бойтесь их. Программисты часто работают с кодом, который непонятно как работает. 

Модификация задачи из книги Х.Дейтела «Как программировать на С»

Подсказка: Внутри строк вывода функций printf не должно быть ни одного пробела, только символы табуляции. В конце строки табуляция не нужна.

Например, код

printf("abc\t\ndef"); и printf("abc\ndef"); выведут на экран

abc
def

Внешне это ничем не отличается, но проверять будет система, для которой невидимые символы табуляции тоже важны. Если обозначить символ табуляции символом *, то вывод будет выглядеть так

printf("abc\t\ndef");
abc*
def

и

printf("abc\ndef");
abc
def

Sample Input:


Sample Output:

N	10*N	100*N	1000*N

1	10	100	1000
2	20	200	2000
3	30	300	3000
4	40	400	4000
5	50	500	5000
6	60	600	6000
7	70	700	7000
8	80	800	8000
9	90	900	9000
10	100	1000	10000


*/

#include <stdio.h> 
int main(void){

  printf("N\t10*N\t100*N\t1000*N\n\n");  
  for (int i=1;i<=10;i++)
    printf("%d\t%d\t%d\t%d\n",i,10*i,100*i,1000*i);

  return(0);
}
