/*

С начала суток прошло kk секунд. Найти количество секунд прошедших с начала последнего часа.

Входные данные:
Целое число kk -- количество секунд прошедших с начала суток.

Выходные данные:
Целое число, равное количеству секунд прошедших с начала последнего часа.

Sample Input:

32792

Sample Output:

392

*/

#include <stdio.h>

int main() {
    int k,s;
    scanf("%d",&k);
    s = k%3600;
    printf("%d",s);
    
    
    return 0;
}
