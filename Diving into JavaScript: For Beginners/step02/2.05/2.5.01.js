/*

Вам нужно вычислить объем сундука. 
Попросите пользователя ввести высоту, ширину и длину сундука и вычислите его объем по формуле высота * ширина * длина. Выведите результат.

Переменные уже объявлены за вас. 

Sample Input 1:

2 
5
5

Sample Output 1:

50

Sample Input 2:

8
2
3

Sample Output 2:

48

Sample Input 3:

9
9
1

Sample Output 3:

81

*/

const height = Number(prompt("Введите высоту сундука:"));
const width = Number(prompt("Введите ширину сундука:"));
const length = Number(prompt("Введите глубину сундука:"));

console.log(height * width * length);
