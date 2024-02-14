/*

Перед вами программа, которая проверяет является ли введенное число четным, используя функциональное выражение. 
Вставьте вместо многоточия инструкцию вызова этой функции и вывода возвращаемого функцией результата.

Sample Input 1:

5

Sample Output 1:

false

Sample Input 2:

8

Sample Output 2:

true

Sample Input 3:

10

Sample Output 3:

true

*/

let a = Number(prompt());
let isEven = function(num){
     return num % 2 === 0;
}
console.log(isEven(a));
