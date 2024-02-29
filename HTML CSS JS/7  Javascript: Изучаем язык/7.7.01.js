/*

    На ввод поступают две строки, необходимо конвертировать их в число, вывести произведение чисел и прибавить два.

x=a∗b+2x=a∗b+2
    Входные данные

    В двух строках вводятся два числа (a и b).
    Выходные данные

    Произведение двух чисел плюс 2(x).

Sample Input 1:

3
6

Sample Output 1:

20

Sample Input 2:

11
6

Sample Output 2:

68

*/

let x = Number(prompt());
let y = Number(prompt());
let z = (x * y) + 2;
console.log(z);
