/*

Последовательность
Вывести последовательность чисел, поступившую на вход.

Входные данные:
На вход программы поступает последовательность целых чисел. Количество чисел в последовательности заранее неизвестно. Но известно, что в конце последовательности записано число -9999 и в последовательности всегда есть хотя бы одно число, кроме -9999.

Выходные данные:
Вывести элементы последовательности на экран через пробел.

Sample Input:

929 440 -77 673 44 -947 -475 -20 919 310 -581 -843 834 532 589 452 -578 -899 11 26 824 -952 -264 254 148 156 -528 280 -9999

Sample Output:

929 440 -77 673 44 -947 -475 -20 919 310 -581 -843 834 532 589 452 -578 -899 11 26 824 -952 -264 254 148 156 -528 280 -9999

*/

#include <stdio.h>

int main(void) {

  int n;

  while(n!=-9999){
	scanf("%d",&n);
	printf("%d ",n);
	}
  
  return 0;
}
