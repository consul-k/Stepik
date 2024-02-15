/*

Напишите программу, которая запрашивает у пользователя ввести строку и символ. 
Программа должна подсчитать, сколько раз данный символ встречается в введенной строке, а затем вывести это количество.

Sample Input 1:

Главное быть самими сабими
а

Sample Output 1:

Символ "а" встречается 3 раз(-а)

Sample Input 2:

шиншилла
ш

Sample Output 2:

Символ "ш" встречается 2 раз(-а)

Sample Input 3:

паприка
г

Sample Output 3:

Символ "г" встречается 0 раз(-а)

*/

let str = prompt();
let s = prompt();
let count = 0;

for (let i = 0; i < str.length; i++) {
  if (str[i] === s) {
      count++;    
  }
}
console.log(`Символ \"${s}\" встречается ${count} раз(-а)`);
