/*

Результатом операции десятичного сдвига вправо для целого числа 127127 будет число 1212. Написать программу, которая осуществляет операцию десятичного сдвига вправо для целого трёхзначного числа kk.

Входные данные:
Целое трёхзначное число kk.

Выходные данные:
Число, полученное из числа kk десятичным сдвигом вправо.

Sample Input:

850

Sample Output:

85

*/

#include <stdio.h>

int main() {
    int x; 
	scanf("%d", &x);
	printf("%d\n", x/10);
    
  return 0;
}
