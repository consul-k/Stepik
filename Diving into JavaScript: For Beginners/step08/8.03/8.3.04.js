/*

Запросите у пользователя ввод имен через запятую с пробелом. Создайте массив из этих имен и используя метод map, 
создайте новый массив, в котором каждое имя будет иметь префикс "Пока, " добавленный перед именем. Затем выведите получившийся массив.

Sample Input 1:

Миша, Вова, Маша, Гоша, Таня

Sample Output 1:

[ 'Пока, Миша', 'Пока, Вова', 'Пока, Маша', 'Пока, Гоша', 'Пока, Таня' ]

Sample Input 2:

Арина, Вика, Асет, Тимур

Sample Output 2:

[ 'Пока, Арина', 'Пока, Вика', 'Пока, Асет', 'Пока, Тимур' ]

*/

let str = prompt();
const strArray = str.split(", ");

const newArray = strArray.map((s) => 'Пока, ' + s);
console.log(newArray);
