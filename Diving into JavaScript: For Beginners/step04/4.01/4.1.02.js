/*

Перед вами программа, которая должна выводить каждое четное число по порядку от 0 до заданного пользователем числа (включительно). 
Напишите вместо многоточия правильное тело цикла. Не используйте условные конструкции.

Sample Input 1:

5

Sample Output 1:

0
2
4

Sample Input 2:

2

Sample Output 2:

0
2

*/

let targetNumber = Number(prompt("Введите число, до которого нужно считать:"));
let currentNumber = 0;

while (currentNumber <= targetNumber) {
   console.log(currentNumber); 
   currentNumber+=2;
}
