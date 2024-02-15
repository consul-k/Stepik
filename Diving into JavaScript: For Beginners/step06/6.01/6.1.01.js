/*

Перед вами объект, в который записывается информация от пользователя об автомобиле.
Выведите эту информацию в соответствии с заявленным форматом.

Sample Input 1:

Audi
A6

Sample Output 1:

Audi A6

Sample Input 2:

Volkswagen
Polo

Sample Output 2:

Volkswagen Polo

Sample Input 3:

Mitsubishi
Lancer

Sample Output 3:

Mitsubishi Lancer

*/

const brand = prompt();
const model = prompt();
let car = {
  brand,
  model,
};
console.log(car.brand, car.model);
