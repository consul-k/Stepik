/*

Напишите программу, которая проверяет, является ли введенное пользователем число положительным. 
Если число положительное, программа выводит сообщение "Положительное", если не положительное - не выводит ничего.

Sample Input 1:

1

Sample Output 1:

Положительное

Sample Input 2:

0

Sample Output 2:

Sample Input 3:

-5

Sample Output 3:

*/

let number = Number(prompt());

if (number > 0) {
    console.log('Положительное');
}
