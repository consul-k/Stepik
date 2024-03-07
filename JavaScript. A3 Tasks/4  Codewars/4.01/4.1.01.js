/*

Напишите функцию, которая вычисляет исходную цену без НДС.

Если цена продукта равна 200, а НДС равен 15%, то окончательная цена (с НДС) составляет:200 + 15% = 230. 
Таким образом, если ваша функция получает 230 в качестве входных данных, она должна вернуть200. 

Примечания

    В этой задаче НДС равен 15%.
    Результат округляется до 2 десятичных знаков.
    
Sample Input 1:

230

Sample Output 1:

200

Sample Input 2:

123

Sample Output 2:

106.96

*/

//return price without vat
function excludingVatPrice(price) {
  let result = price / 1.15;
    return Math.round(result*100)/100;
  return 0;
}

const price = Number(prompt())
console.log(excludingVatPrice(price))
