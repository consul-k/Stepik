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
