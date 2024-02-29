/*

Ваша функция должна вернуть все делители числа в виде массива чисел.

Sample Input 1:

8

Sample Output 1:

[ 1, 2, 4, 8 ]

Sample Input 2:

2

Sample Output 2:

[ 1, 2 ]

Sample Input 3:

48

Sample Output 3:

[ 1, 2, 3, 4, 6, 8, 12, 16, 24, 48 ]

*/

function delimiters(num){
    let arr = [1,];
    for (let i = 2; i <= num; i++) {
        if(num%i===0) {
            arr.push(i);
        }
    }
    return arr;
}
