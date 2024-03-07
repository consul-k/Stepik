/*

Вычислить факториал для числа. На всякий случай напоминаем, что факториал числа a это произведение всех целых чисел от 1 до a, 
например, если а = 5, то факториал a будет равен 1 * 2 * 3 * 4 * 5

Sample Input 1:

7

Sample Output 1:

5040

Sample Input 2:

9

Sample Output 2:

362880

*/

function testFactorial(a) {
    let x;
    x = 1;
    for (let i = 1; i <= a; i++) {
        x *= i;
    }
    return x;
    return x;
}

let a = Number(prompt())
console.log(testFactorial(a))
