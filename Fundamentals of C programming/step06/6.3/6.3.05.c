/*
Кнопочный электронный кодовый замок имеет десять кнопок. Каждая из кнопок имеет свой порядковый номер от 0 до 9. Правильный код 1024 зашит внутрь замка. Человек, который хочет открыть дверь, должен ввести на циферблате последовательно 1, 0, 2 и 4. Напишите программу, моделирующую работу такого замка.

Входные данные:
Четыре целых числа b1,b2,b3,b4b1​,b2​,b3​,b4​ -- номера кнопок, которые нажал человек.

Выходные данные:
Строка open, если введён правильный код. Строка close, если введён неправильный код.


Sample Input 1:

1 0 2 4

Sample Output 1:

open

Sample Input 2:

1 0 2 3

Sample Output 2:

close

*/

#include <stdio.h>

int main() {
  int b1,b2,b3,b4;
  scanf("%d %d %d %d",&b1,&b2,&b3,&b4);
    
  if (b1 == 1 && b2 == 0 && b3 == 2 && b4 == 4) {
	  printf("open");
     } else 
	   printf("close");
    
  return 0;
}
