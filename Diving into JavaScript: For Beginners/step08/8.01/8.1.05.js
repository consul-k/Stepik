/*

Перед вами программа, которая сначала запрашивает количество элементов массива, а затем элементы массива по одному соответствующее количество раз. 
Программа добавляет каждый элемент, введенный пользователем, в конец массива. 
Далее, с помощью цикла for...of в массив lengths поочерёдно добавляются длина каждого элемента массива userArray.  
Заполните тела циклов так, чтобы программа работала.

Sample Input 1:

3
killa
kot
oshparenny

Sample Output 1:

[ 5, 3, 10 ]

Sample Input 2:

6
A
AAA
AA
AAAA
AAAA
AAAA

Sample Output 2:

[ 1, 3, 2, 4, 4, 4 ]

Sample Input 3:

2
Iphone
Ipod

Sample Output 3:

[ 6, 4 ]

*/

const numElements = Number(prompt("Введите количество элементов в массиве:"));
const userArray = [];
const lengths = [];

for (let i = 0; i < numElements; i++) {
    userArray.unshift(prompt());
}

for (const word of userArray) {
    lengths.unshift(word.length);
}

console.log(lengths);
