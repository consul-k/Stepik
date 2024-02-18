/*

Создайте массив users, запросите у пользователя ввод двух имен и добавьте их в массив. Затем выведите обновленный массив

Sample Input 1:

Фирамир
Азлагор

Sample Output 1:

[ 'Фирамир', 'Азлагор' ]

Sample Input 2:

Ирина
Матвей

Sample Output 2:

[ 'Ирина', 'Матвей' ]

Sample Input 3:

Амина
Алина

Sample Output 3:

[ 'Амина', 'Алина' ]

*/

const arr = [];

let name1 = prompt();
let name2 = prompt();

arr.unshift(name1, name2);
console.log(arr);
