/*

Перед вами программа, которая сначала запрашивает количество элементов массива, 
а затем элементы массива по одному соответствующее количество раз. 
Программа добавляет каждый элемент, введенный пользователем, в начало массива и выводит получившийся массив. 
Заполните тело цикла так, чтобы программа работала.

Sample Input 1:

2
Lenovo
Samsung

Sample Output 1:

[ 'Samsung', 'Lenovo' ]

Sample Input 2:

5
user1
user2
user3
user4
user5

Sample Output 2:

[ 'user5', 'user4', 'user3', 'user2', 'user1' ]

Sample Input 3:

3
1
2
3

Sample Output 3:

[ '3', '2', '1' ]

*/

const numElements = Number(prompt("Введите количество элементов в массиве:"));
const userArray = [];

for (let i = 0; i < numElements; i++) {
    let element = prompt();
    userArray.unshift(element);
}

console.log(userArray);
