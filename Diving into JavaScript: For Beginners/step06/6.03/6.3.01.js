/*

Создайте объект c единственным методом, который принимает два числа, введенных пользователем, 
как параметры и выводит остаток от деления первого числа на второе. 

Sample Input 1:

5
2

Sample Output 1:

1

Sample Input 2:

9
3

Sample Output 2:

0

Sample Input 3:

7
5

Sample Output 3:

2

*/

let n1 = Number(prompt());
let n2 = Number(prompt());

let calc = {
    d(a,b) {
        console.log(a%b);
    }
};

calc.d(n1,n2);
