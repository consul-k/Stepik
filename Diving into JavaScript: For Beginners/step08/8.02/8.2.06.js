/*

    Запросите у пользователя произвольные значения через запятую с пробелом и поместите их в массив.
    Далее, запросите у пользователя индексы элементов, которые они хотят вывести и в каком порядке через запятую.
    Выведите через пробел запрошенные элементы массива.

Sample Input 1:

1, 2, 3
0, 2, 1

Sample Output 1:

1 3 2

Sample Input 2:

11, 12, 13, 14
0, 3

Sample Output 2:

11 14

Sample Input 3:

моя, мелодия, уже, не, моя
1, 4

Sample Output 3:

мелодия моя

*/

let str = prompt();
const strArray = str.split(", ");

let num = prompt();
const numArray = num.split(", ");
const newArray = []

for (const num of numArray) {
    newArray.push(strArray[num]);
}

const res = newArray.join(' ');
console.log(res);
