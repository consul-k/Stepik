/*

Найти частное произведений цифр, соответствующих четным и нечетным разрядам четырехзначного числа.

Входные данные:
Натуральное четырёхзначное число A=a4a3a2a1A=a4​a3​a2​a1​

Выходные данные:
Вещественное число хх, полученное от деления произведения цифр четных разрядов числа А на произведение цифр нечётных разрядов числа А. Формат вывода 2 знака после запятой.

Sample Input:

3421

Sample Output:

1.50

*/

#include <stdio.h>

int main() {
  int k,a,b;
  double a1,a2;
  scanf("%d",&k);
	
  a = (int)k/1000;
  b = (int)k%100/10;
  a1 = a*b;

  a = (int)k/100%10;
  b = (int)k%10;
  a2 = a*b;

  printf("%.2lf",a1/a2);

  return 0;
}
