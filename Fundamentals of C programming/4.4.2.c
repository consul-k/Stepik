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
