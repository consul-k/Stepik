/*

Перед вами объект catalogue, в котором содержится свойство magazine: 5. 
Удалите это свойство из объекта и добавьте в объект свойство newspaper с числовым значением, которое пользователь вводит самостоятельно. 
Выведите значение свойства newspaper. 

Sample Input 1:

777

Sample Output 1:

777

Sample Input 2:

123

Sample Output 2:

123

Sample Input 3:

6

Sample Output 3:

6

*/

const catalogue = {
    magazine: 5,
};
delete catalogue.magazine;
let n = Number(prompt());
catalogue.newspaper = n;

console.log(catalogue.newspaper);
