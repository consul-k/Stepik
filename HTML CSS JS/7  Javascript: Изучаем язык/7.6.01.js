/*

    На вход подается два числа разделённых точкой. Выведите их без точки.
Для принятия входных значений используйте prompt()

Sample Input 1:

8.11

Sample Output 1:

8 11

Sample Input 2:

-1.2

Sample Output 2:

-1 2

*/

let [a, b] = prompt().split(".");
console.log(a, b);
