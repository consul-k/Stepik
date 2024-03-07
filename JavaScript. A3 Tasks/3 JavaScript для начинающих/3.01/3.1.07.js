/*

Вписать в указанное место код, который будет присваивать переменной "х" название цифры, переданной в переменную "а". 
Цифра в переменную "а" будет передана случайным образом и может оказаться в диапазоне от 0 до 9 включительно, 
название должно быть написано по-русски с большой буквы - "Ноль", "Один", "Два" и т.д.

Sample Input:

2

Sample Output:

Два

*/

function testCase(a) {
    let x;
    switch (a) { 
        case 0:
            x= "Ноль";
            break;
        case 1:
            x= "Один";
            break;
        case 2:
            x= "Два";
            break;
        case 3:
            x="Три";
            break;
        case 4:
            x="Четыре";
            break;
        case 5:
            x="Пять";
            break;
        case 6:
            x="Шесть";
            break;
        case 7:
            x="Семь";
            break;
        case 8:
            x="Восемь";
            break;
        case 9:
            x="Девять";
            break; }
    return x;
}

let a = Number(prompt())
console.log(testCase(a))
