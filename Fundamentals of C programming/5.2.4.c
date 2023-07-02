/*

Определить равны ли нулю все введённые числа.

Входные данные:
Пять целых чисел: x1,x2,x3,x4,x5x1​,x2​,x3​,x4​,x5​. (−100≤xi≤100)(−100≤xi​≤100)

Выходные данные:
Число 00, если все числа x1,x2,x3,x4,x5x1​,x2​,x3​,x4​,x5​ равны нулю, иначе положительное число, формируемое по определенному правилу, которое вам предстоит сформулировать самостоятельно. Анализируя вход и выход для примеров ниже, вам нужно понять, как из входных данных получаются выходные. Попытайтесь понять, как работает этот чёрный ящик.

Sample Input 1:

2 0 0 0 0

Sample Output 1:

4

Sample Input 2:

0 3 0 2 0

Sample Output 2:

13

*/

#include <stdio.h>

int main() {
  int x,n=5,c1=0,c2=0;
  scanf("%d",&x);
    
  while (n!=0) {
    if (x!=0) {
		c1=x*x;
    	c2=c2+c1;
    }
    n--;
    scanf("%d",&x);
  }
    printf("%d",c2);
    
  return 0;
}
