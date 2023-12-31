/*

Сравнение чисел по модулю. Обычно мы сравниваем числа между собой напрямую. Но в математике и криптографии частенько используется сравнение по модулю целого числа kk. Два числа сравнимы по модулю kk, если равны их остатки от деления на kk. Например, числа 33 и 99, сравнимы по модулю 66, а числа 2525 и 1313 сравнимы по модулю 33. Напишите программу, которая помогает сравнивать числа по модулю kk.

Входные данные:
Три натуральных числа:
Первое число kk -- модуль, по которому необходимо сравнить числа. Второе и третье -- числа, которые необходимо сравнить по модулю kk

Выходные данные:
Два числа: остатки от деления на kk

Sample Input:

20 864 910

Sample Output:

4 10

*/

#include <stdio.h>
int main(void){
int k, x, y;
    
    scanf("%d%d%d", &k, &x, &y);
    printf("%d %d", x % k, y % k);
    
return 0;
}
