/*

Числа Фибоначчи
Последовательность чисел Фибоначчи определяется следующим образом:
F1=1,F2=1,
F1​=1,F2​=1,
F3=F1+F2,…,Fk=Fk−2+Fk−1.
F3​=F1​+F2​,…,Fk​=Fk−2​+Fk−1​. Посчитать значение NN-го числа Фибоначчи.

Входные данные:
Одно натуральное число NN, (N≤45)(N≤45)

Выходные данные:
Значение NN-го числа Фибоначчи.

Sample Input:

45

Sample Output:

1134903170

*/

#define _CRT_SECURE_NO_WARNINGS                          
#include <stdio.h>

int main()
{
    double N, F1 = 0, F2 = 1, F3 = 0;
    scanf("%lf", &N);
    
    if ((N > 0) && (N <= 2))
    {
        printf("%.lf", F2);
    }
    else
    {
        if ((N>0)&&(N <= 45))
        {
            for (N; N > 1; N = N - 1)
            {
                F3 = F1 + F2;
                F1 = F2;
                F2 = F3;

            } printf("%.lf\n", F3);
        }
    }
    return 0;
}
