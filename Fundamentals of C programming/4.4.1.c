#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(void){
    srand(time(NULL));
    int rand_digit = rand()%2;
    printf("%d\n",rand_digit);
    return 0;
}
