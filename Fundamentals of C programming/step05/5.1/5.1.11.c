/*

Факториал
Факториалом натурального числа NN называют произведение всех натуральных чисел от 11 до NN включительно. Факториал обозначают значком !! после числа.
Например:
3!=1⋅2⋅33!=1⋅2⋅3 -- факториал трёх
5!=1⋅2⋅3⋅4⋅55!=1⋅2⋅3⋅4⋅5 -- факториал пяти

Напишите программу, которая вычисляет значение факториала для первых 10 чисел.

Входные данные:
отсутствуют

Выходные данные:
10 строк вида. Поле под значение факториала −− 8 символов.

1! =       1
2! =       2
3! =       6

и т.д.

Sample Input:


Sample Output:

1! =       1
2! =       2
3! =       6
4! =      24
5! =     120
6! =     720
7! =    5040
8! =   40320
9! =  362880
10!= 3628800

*/

#include <stdio.h>

int main() {
  int a1,a2,a3,a4,a5,a6,a7,a8,a9,a10;
  a1 = 1;
  printf("%d",1);
  printf("! =");
  printf("%8d\n",a1);
  a2 = 1*2;
  printf("%d",2);
  printf("! =");
  printf("%8d\n",a2);
  a3 = 1*2*3;
  printf("%d",3);
  printf("! =");
  printf("%8d\n",a3);
  a4 = 1*2*3*4;
  printf("%d",4);
  printf("! =");
  printf("%8d\n",a4);
  a5 = 1*2*3*4*5;
  printf("%d",5);
  printf("! =");
  printf("%8d\n",a5);
  a6 = 1*2*3*4*5*6;
  printf("%d",6);
  printf("! =");
  printf("%8d\n",a6);
  a7 = 1*2*3*4*5*6*7;
  printf("%d",7);
  printf("! =");
  printf("%8d\n",a7);
  a8 = 1*2*3*4*5*6*7*8;
  printf("%d",8);
  printf("! =");
  printf("%8d\n",a8);
  a9 = 1*2*3*4*5*6*7*8*9;
  printf("%d",9);
  printf("! =");
  printf("%8d\n",a9);
  a10 = 1*2*3*4*5*6*7*8*9*10;
  printf("%d",10);
  printf("!=");
  printf("%8d\n",a10);
  

  return 0;
}
