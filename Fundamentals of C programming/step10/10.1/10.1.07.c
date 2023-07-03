/*

Квадрат.
Напишите функцию с именем square(n,c), которая выводит на экран квадрат размера n на n, заполненный символами c. Например:

square(4,'#');
выведет:
####
####
####
####

Входные данные:
Одно целое число и символ заполнитель.

Выходные данные:
Квадрат из символов, указанного формата.

Sample Input 1:

3 #

Sample Output 1:

###
###
###

Sample Input 2:

5 .

Sample Output 2:

.....
.....
.....
.....
.....

Sample Input 3:

8 *

Sample Output 3:

********
********
********
********
********
********
********
********

Sample Input 4:

6 %

Sample Output 4:

%%%%%%
%%%%%%
%%%%%%
%%%%%%
%%%%%%
%%%%%%

*/

#include <stdio.h>
void square(int x, char c){
   int i,z;
   for(i=0;i<x;i++) {
       for(z=0;z<x;z++){
       printf("%c",c);
       }
   if (z==x){
    printf("\n");
    }
   }
}
int main(){ 
    int x;
    char c;
    scanf("%d %c",&x,&c);
    square(x,c);
    
    return 0;
}
