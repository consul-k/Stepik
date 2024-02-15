/*

Напишите программу, которая запрашивает у пользователя строку и затем выводит эту строку в обратном порядке и в нижнем регистре.

Sample Input 1:

Палка

Sample Output 1:

аклап

Sample Input 2:

У пожилого

Sample Output 2:

оголижоп у

Sample Input 3:

Улыбок

Sample Output 3:

кобылу

*/

const sentence = prompt().toLowerCase();
let new_sent = '';

for (let i = sentence.length-1; i >= 0 ; i--) {
  new_sent+=sentence[i];
}
console.log(new_sent);
