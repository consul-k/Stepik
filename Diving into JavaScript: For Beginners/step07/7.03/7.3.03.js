/*

Напишите программу, которая запрашивает у пользователя ввод произвольной строки, 
а затем выводит каждый второй символ этой строки на отдельной строке в верхнем регистре.

Sample Input 1:

Жаба

Sample Output 1:

А
А

Sample Input 2:

годовщина

Sample Output 2:

О
О
Щ
Н

*/

const sentence = prompt();
for (let i = 1; i < sentence.length; i+=2) {
  console.log(sentence[i].toUpperCase());
}
