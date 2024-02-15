/*

Перед вами объект, который содержит значение основания. Добавьте в объект метод, который принимает от пользователя число Y, 
как параметр и возводит число Y - 2 в степень Y. Напишите инструкции ввода числа Y и вывода результата выполнения метода.

Sample Input 1:

4

Sample Output 1:

16

Sample Input 2:

5

Sample Output 2:

243

Sample Input 3:

3

Sample Output 3:

1

*/

let Y = Number(prompt());
const calculator = {
    base: Y - 2,
    power() {
        console.log(this.base**Y);
    }
};
calculator.power(Y);
