/*

Написать программу — модель анализа пожарного датчика в помещении, которая выводит сообщение Fire situation, если температура в комнате превысила 60 градусов по Цельсию.

Входные данные:
Одно целое число TT -- температура в помещении.

Выходные данные:
Строка Fire situation, если T>60T>60. В противном случае ничего выводить не нужно.

*/

#include <stdio.h>

int main() {
  int t;
  scanf("%d",&t);
  
  if (t > 60)
    printf("Fire situation\n");
 
  return 0;
}
