/*

Масса одной молекулы воды приблизительно равна 3×10−233×10−23 грамм.  Масса одной капли воды приблизительно 0.050.05 гр. В одном гранёном стакане ≈249.5≈249.5 гр.  Напишите программу, которая вычисляет количество капель и молекул воды в NN гранёных стаканах воды.

Входные данные:
Натуральное число NN −− количество стаканов воды.

Выходные данные:
Два числа.  Первое число −− целое число количества капель в NN стаканах воды. Второе число −− количество молекул воды в NN стаканах воды. Точность −− 3 знака после запятой.

Справка:
Для вывода вещественного числа используйте спецификатор формата %e.
Для объявления очень малых/больших переменных используйте научный формат записи чисел.

double x = 3e-23;

Sample Input 1:

1

Sample Output 1:

4990 8.317e+24

Sample Input 2:

3

Sample Output 2:

14970 2.495e+25

*/

#include <stdio.h>
int main()
{
    int N;
    double mw = 0.05, ms = 249.5, k, m = 3e-23, result;
    
    scanf(" %d", &N);
    result = (ms / mw) * N;
    k = ((mw / m) * result);
    printf("%.0lf %.3e", result, k);
    printf("\n");
    return 0;
}
