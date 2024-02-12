/*

Напишите программу для оценки настроения на основе введенного пользователем числа от 1 до 10.

    1-3 - программа выводит "Плохое" 
    4-7 - программа выводит "Нормальное"
    8-10 - программа выводит "Хорошее"

Если пользователь ввел число вне диапазона, программа выводит "Число вне диапазона"

Sample Input 1:

10

Sample Output 1:

Хорошее

Sample Input 2:

3

Sample Output 2:

Плохое

Sample Input 3:

5

Sample Output 3:

Нормальное

Sample Input 4:

11

Sample Output 4:

Число вне диапазона

*/

let mood = Number(prompt());

if (mood >= 1 && mood <= 3) {
    console.log('Плохое');
}
else if (mood >= 4 && mood <= 7) {
    console.log('Нормальное');
}
else if (mood >= 8 && mood <= 10){
    console.log('Хорошее');
}
else {
    console.log('Число вне диапазона');
}
