/*

Запросите у пользователя произвольные значения через запятую с пробелом. 
Поместите их в массив и переведите в числовой тип данных. Выведите массив.

Sample Input 1:

1, 2, три, 4, пять

Sample Output 1:

[ 1, 2, 'три', 4, 'пять' ]

Sample Input 2:

6, 0, p, u, c

Sample Output 2:

[ 6, 0, 'p', 'u', 'c' ]

Sample Input 3:

777, 888, 999

Sample Output 3:

[ 777, 888, 999 ]

*/

let str = prompt();
const strArray = str.split(", ");
const newArray = [];

for (const s of strArray) {
    if (isNaN(s)) {
        newArray.push(s);
    } else {
        newArray.push(parseInt(s));
    }
}

console.log(newArray);
