/*

Напишите программу, которая выводит на экран числа от 1 до 100. При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz», а вместо чисел, кратных пяти — слово «Buzz». Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz»

Входные данные:
Отсутствуют

Выходные данные:
См.пример выходных данных

Sample Input:


Sample Output:

1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 FizzBuzz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 FizzBuzz 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 FizzBuzz 76 77 Fizz 79 Buzz Fizz 82 83 Fizz Buzz 86 Fizz 88 89 FizzBuzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz

*/

#include <stdio.h>

int main() {
 int i = 0;

	for (i = 1; i < 101; i++)
		if (i%3 == 0 && i%5 == 0)
			printf("FizzBuzz ");
		else if (i%3 == 0)
			printf("Fizz ");
		else if (i%5 == 0)
			printf("Buzz ");
		else
			printf("%d ", i);

  
  return 0;
}

