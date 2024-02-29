/*

Вводится число n. Затем элементы матрицы n на n.

Вам нужно вывести все числа, больше или равные среднему арифметическому матрицы.

    Каждое число нужно выводить с новой строки.

    Числа выводить в порядке обхода матрицы слева направо, сверху вниз.

Sample Input:

3
3 7 5
1 5 9
0 7 8

Sample Output:

7
5
5
9
7
8

*/

let n = Number(prompt());
let matrix = [];
let average = 0;

for(let i = 0; i<n; i++){
   matrix[i] = prompt().split(" ").map(Number);
}
for(let i = 0; i<n; i++){
    for(let j = 0; j<n; j++){
        average += matrix[i][j];
    }
}

average = average/(n*n);

for(let i = 0; i<n; i++){
    for(let j = 0; j<n; j++){
        if(matrix[i][j] >= average)
            console.log(matrix[i][j]);
    }
}
