/*

Дополните спецификаторы формата соответствующими модификаторами, чтобы вывод на экран выглядел следующим образом:
 

||-----|-----|-----|-----|| || act | one | two | res || ||=====+=====+=====+=====|| || +|3 |4 |00007|| || -| 3| 4|-0001|| || *| 3|4 |00012|| ||/ |3 | 4|0.750|| ===========================

Sample Input:


Sample Output:

||-----|-----|-----|-----||
|| act | one | two | res ||
||=====+=====+=====+=====||
||    +|3    |4    |00007||
||    -|    3|    4|-0001||
||    *|    3|4    |00012||
||/    |3    |    4|0.750||
===========================


*/

#include <stdio.h> 
int main(void){
  int a=3, b=4;
  double res = 0.75;

  printf("||-----|-----|-----|-----||\n");
  printf("|| act | one | two | res ||\n");
  printf("||=====+=====+=====+=====||\n");
  printf("||%5c|%-5d|%-5d|%5.5d||\n",'+',a,b,a+b);
  printf("||%5c|%5d|%5d|%5.4d||\n",'-',a,b,a-b);
  printf("||%5c|%5d|%-5d|%5.5d||\n",'*',a,b,a*b);
  printf("||%-5c|%-5d|%5d|%1.3f||\n",'/',a,b,res);
  printf("===========================");

  return(0);
}
