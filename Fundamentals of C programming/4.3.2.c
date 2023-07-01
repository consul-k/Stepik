/*

В выражении

a/b*c/d*e/f*h

расставить скобки так, чтобы выражению со скобками соответствовала дробь https://ucarecdn.com/8eb75619-9396-43ca-bdc1-8f0f94493d4b/

Входные данные: семь целых чисел a,b,c,d,e,fa,b,c,d,e,f и hh соответственно.

Выходные данные: ﻿результат выражения. Точность  2 знака после запятой.

Источник: С.А. Абрамов, Е.В. Зима "Начало программирования на языке Паскаль"

Sample Input:

7 2 3 7 8 3 4

Sample Output:

5.44

*/

#include <stdio.h>
#include <math.h>
int main(void){
  double a, b, c, d, e, f, h;
  double res;
  scanf("%lf",&a);
  scanf("%lf",&b);
  scanf("%lf",&c);
  scanf("%lf",&d);
  scanf("%lf",&e);
  scanf("%lf",&f);
  scanf("%lf",&h);

  res = (double)(a/(b*(c/(d*(e/(f*h))))));  
  printf("%.2lf", res);

  return 0;
}
