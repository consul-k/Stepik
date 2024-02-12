/*

Запросите у пользователя число x, а затем число y. Проверьте является ли х больше чем у. 
Выведите результат проверки (true или false). 

Sample Input 1:

8
11

Sample Output 1:

false

Sample Input 2:

65
15

Sample Output 2:

true

Sample Input 3:

5
5

Sample Output 3:

false

*/

let x = Number(prompt());
let y = Number(prompt());

let isGreater = x > y;
console.log(isGreater);
