/*

Факториал.
Напишите функцию с именем factorial, которая вычисляет факториал числа, переданного ей в качестве аргумента.

Входные данные:
Одно целое неотрицательное число N,(N<13)N,(N<13).

Выходные данные:
Одно целое число, факториал исходного числа.

Sample Input:

5

Sample Output:

120

*/

int main(void){
    int n;
    
    scanf("%d",&n);
    
    printf("%d",factorial(n));
    
    return 0;
}

int factorial(int n){
    int f=1;
	int c;

    for (c = 1; c <= n; c++) {
    f = f * c;
    }
    
    return f;
}
