/*

На вход программе подаётся два числа S и E, записанных через пробел. При этом гарантируется, что S≤ES≤E. Программа должна выводить одно случайное число из промежутка [S;E][S;E]

Sample Input:

141 273

Sample Output:

233

*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(void){
	int s,e;
	scanf("%d",&s);
	scanf("%d",&e);
    srand(time(NULL));
    int rand_digit = s + rand()%(e-s+1);
    printf("%d\n",rand_digit);
    return 0;
}
