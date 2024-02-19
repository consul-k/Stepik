/*

    Запросите у пользователя произвольные значения через запятую с пробелом и поместите их в массив
    Далее, запросите у пользователя начальный и конечный индексы (включительно) поочерёдно для среза массива. 
    Используя метод slice, создайте новый массив, содержащий элементы, указанные пользователем, 
    и выведите элементы массива через запятую с пробелом.

Sample Input 1:

я, ты, мы, он
1
2

Sample Output 1:

ты, мы

Sample Input 2:

Бразилия, Россия, Индия, Китай, Южная Африка
2
3

Sample Output 2:

Индия, Китай

Sample Input 3:

прив, кд, чд
1
1

Sample Output 3:

кд

*/

let str = prompt();
const strArray = str.split(", ");

let n1 = Number(prompt());
let n2 = Number(prompt());

const newArray = strArray.slice(n1, n2+1);
const newString = newArray.join(', ');
console.log(newString);
