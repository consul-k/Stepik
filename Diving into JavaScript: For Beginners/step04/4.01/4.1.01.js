/*

Перед вами программа, которая должна выводить каждое число по порядку от 1 до заданного пользователем числа (включительно). 
Напишите вместо многоточия правильное условие.

Sample Input 1:

3

Sample Output 1:

1
2
3

Sample Input 2:

6

Sample Output 2:

1
2
3
4
5
6

Sample Input 3:

2

Sample Output 3:

1
2

*/

let targetNumber = Number(prompt("Введите число, до которого нужно считать:"));
let currentNumber = 1;

while (currentNumber <= targetNumber) {
  console.log(currentNumber);
  currentNumber++;
}
