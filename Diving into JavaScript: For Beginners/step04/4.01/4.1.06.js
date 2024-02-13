/*

Напишите программу, которая запрашивает у пользователя сначала число num1, а затем число num2. 
Если num1 больше num2, программа выводит все числа, кратные 3, по порядку от num1 до num2 включительно от большего к меньшему. 
Если num1 меньше num2, программа выводит все числа, кратные 3, от num1 до num2 включительно от меньшего к большему.

Sample Input 1:

2
7

Sample Output 1:

3
6

Sample Input 2:

30
20

Sample Output 2:

30
27
24
21

Sample Input 3:

9
6

Sample Output 3:

9
6

*/

let num1 = Number(prompt());
let num2 = Number(prompt());

if (num1 > num2) {
    while (num1>=num2) {
        if (num1%3==0){
            console.log(num1);
        } 
        num1--;
    }
} else {
    while (num1<=num2) {
        if (num1%3==0){
            console.log(num1);
        } 
        num1++;
    }
}
