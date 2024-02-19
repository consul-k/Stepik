/*

    Запросите у пользователя произвольные значения через запятую с пробелом и поместите их в массив.
    Далее, запросите у пользователя индексы элементов, которые они хотят вывести и в каком порядке через запятую.
    Выведите поочерёдно на новой строке запрошенные элементы массива.

Sample Input 1:

1, 2, 3
0, 2, 1

Sample Output 1:

1
3
2

Sample Input 2:

хейзы, шмейзы, амнезия
1, 2

Sample Output 2:

шмейзы
амнезия

Sample Input 3:

11, 12, 13, 14
0, 3

Sample Output 3:

11
14

*/

let str = prompt();
const strArray = str.split(", ");

let num = prompt();
const numArray = num.split(", ");

for (const num of numArray) {
    console.log(strArray[num]);
}
