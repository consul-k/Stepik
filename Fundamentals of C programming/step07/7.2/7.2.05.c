/*

Максимум и минимум
Необходимо найти максимальный и минимальный элемент последовательности, неизвестной длины.

Входные данные:
Последовательность целых чисел, оканчивающаяся нулём. Само число нуль не является членом последовательности, а является лишь сигналом того, что достигнут конец последовательности. В последовательности есть как минимум одно ненулевое число.

Выходные данные:
Вывести два целых числа MM и mm, где MM - максимальный элемент последовательности, mm - минимальный элемент последовательности.

Sample Input 1:

123 443 652 828 2 4212 0

Sample Output 1:

4212 2

Sample Input 2:

3 0

Sample Output 2:

3 3

*/

#include <stdio.h>

int main(void) {

  int min=9999,max=-9999,number = 1;
  scanf("%d", &number);

  while (number!=0) {
    
    if (number >= max)
        max = number;
    if (min >= number)
        min = number;
	scanf("%d", &number);
  }

  printf("%d %d\n", max, min);

  return 0;
}
