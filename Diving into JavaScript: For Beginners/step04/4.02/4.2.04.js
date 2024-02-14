/*

Напишите программу, которая будет запрашивать у пользователя два целых числа, начальное значение A и конечное значение B. 
Затем программа должна вывести на экран все целые числа в диапазоне от B до A в обратном порядке.

Sample Input 1:

3
8

Sample Output 1:

8
7
6
5
4
3

Sample Input 2:

2
5

Sample Output 2:

5
4
3
2

*/

let a = Number(prompt());
let b = Number(prompt());

for (let i = b; i >= a; i--) {
  console.log(i);
}
