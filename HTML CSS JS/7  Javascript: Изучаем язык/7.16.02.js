/*

На вход вашей функции будет подаваться 2 числа - a и b.
    Функция должна вернуть сумму чисел от a до b включительно.

a <= b

Sample Input 1:

2
4

Sample Output 1:

9

Sample Input 2:

1
10

Sample Output 2:

55

Sample Input 3:

1
100

Sample Output 3:

5050

*/

function summ(a, b){
    let arr = 0;
    for (let i = a; i <= b; i++) {
        arr+=i
    }
    return arr;
}
