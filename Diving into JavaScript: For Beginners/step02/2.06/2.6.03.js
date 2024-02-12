/*

Запросите у пользователя число x,  затем число y, а затем число z. 
Проверьте сумму x и y на строгое равенство с суммой y и z. Выведите результат проверки (true или false). 

Sample Input 1:

7
6
5

Sample Output 1:

false

Sample Input 2:

3
2
3

Sample Output 2:

true

*/

let x = Number(prompt());
let y = Number(prompt());
let z = Number(prompt());

console.log(x+y === y+z);
