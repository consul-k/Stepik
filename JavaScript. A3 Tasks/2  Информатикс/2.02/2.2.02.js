/*

Следующее предыдущее

Напишите программу, которая считывает целое число и выводит текст, аналогичный приведенному в примере.

Пробелы, знаки препинания, заглавные и строчные буквы важны!

Входные данные

Вводится целое число.

Выходные данные

Выведите ответ на задачу.

Sample Input 1:

179

Sample Output 1:

The next number for the number 179 is 180.
The previous number for the number 179 is 178.

Sample Input 2:

2

Sample Output 2:

The next number for the number 2 is 3.
The previous number for the number 2 is 1.

*/


let n = Number(prompt());
console.log(`The next number for the number ${n} is ${n+1}.`);
console.log(`The previous number for the number ${n} is ${n-1}.`);
