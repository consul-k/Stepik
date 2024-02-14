/*

Напишите программу, которая запрашивает у пользователя четыре числа и объявляет функцию compareAndPrintMax. 
Эта функция принимает четыре числа как параметры и сравнивает их, затем выводит сообщение о том, какое число больше.

Sample Input 1:

4
5
6
2

Sample Output 1:

6

Sample Input 2:

7
6
5
12

Sample Output 2:

12

Sample Input 3:

5
3
4
9

Sample Output 3:

9

*/

let num1 = Number(prompt());
let num2 = Number(prompt());
let num3 = Number(prompt());
let num4 = Number(prompt());

function compareAndPrintMax(Num1, Num2, Num3, Num4) {
	if (Num1 > Num2 && Num1 > Num3 && Num1 > Num4) {
		console.log(Num1);
	} else if (Num2 > Num1 && Num2 > Num3 && Num2 > Num4) {
		console.log(Num2);
	} else if (Num3 > Num1 && Num3 > Num2 && Num3 > Num4) {
		console.log(Num3);
	} else {
		console.log(Num4);
	}
}
compareAndPrintMax(num1, num2, num3, num4);
