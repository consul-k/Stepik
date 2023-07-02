/*

Найти среднее арифметическое элементов массива.

Входные данные:
Первая строка число N,(N>0)N,(N>0) -- длина массива. Длина массива не более 100 элементов. Вторая строка NN  натуральных чисел, записанных через пробел

Выходные данные:
Одно вещественное число MM -- среднее арифметическое элементов массива. Формат вывода -- два знака после запятой.

Sample Input 1:

5
10 93 22 75 12

Sample Output 1:

42.40

Sample Input 2:

4
4 3 2 1

Sample Output 2:

2.50

*/

#include <stdio.h>

int main(void) {  
  int n=0,count=0;
  double m=0;
  int num[100] = {0};
  
  scanf("%d",&count);

  for(int i = 0; i <= count; i = i + 1){
    scanf("%d",&n);
    num[i] = num[i] + n;
  }

  for(int s = 0; s < count; s = s + 1){
      m = m + num[s];
  }

  printf("%.2lf",m/count);


  return 0;
}
