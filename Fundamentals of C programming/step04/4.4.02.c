/*

Поле для игры в рулетку состоит из ячеек от 0 до N.  На вход программе подаётся одно натуральное число N.

Программа должна выдать случайное число от нуля до N.

Sample Input:

36

Sample Output:

36

*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(void){
	int n;
	scanf("%d",&n);
    srand(time(NULL));
    int rand_digit = rand()%n;
    printf("%d\n",rand_digit);
    return 0;
}
