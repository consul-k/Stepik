/*

Напишите программу, которая запрашивает у пользователя сначала число num1, а затем число num2. 
Если num1 больше num2, программа выводит все числа по порядку от num1 до num2 включительно от большего к меньшему. 
Если num1 меньше num2, программа выводит все числа по порядку от num1 до num2 включительно от меньшего к большему.

Sample Input 1:

12
16

Sample Output 1:

12
13
14
15
16

Sample Input 2:

5
3

Sample Output 2:

5
4
3

*/

let num1 = Number(prompt());
let num2 = Number(prompt());

if (num1 > num2) {
    while (num2 <= num1){
    console.log(num1);
    num1--;
    }
} else {
    while (num1 <= num2){
    console.log(num1);
    num1++;
    }
}
