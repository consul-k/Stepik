/*

Запросите у пользователя строковые значения через пробел и поместите их в массив. 
Используя метод map, создайте новый массив, который будет содержать эти значения, написанные заглавными буквами.

Sample Input 1:

do a barrel roll

Sample Output 1:

[ 'DO', 'A', 'BARREL', 'ROLL' ]

Sample Input 2:

смотреть онлайн бесплатно

Sample Output 2:

[ 'СМОТРЕТЬ', 'ОНЛАЙН', 'БЕСПЛАТНО' ]

Sample Input 3:

молоко сахар бетон бабушка

Sample Output 3:

[ 'МОЛОКО', 'САХАР', 'БЕТОН', 'БАБУШКА' ]

*/

let str = prompt();
const strArray = str.split(" ");

const newArray = strArray.map((s) => s.toUpperCase());
console.log(newArray);
