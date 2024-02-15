/*

Напишите программу, которая запрашивает ввод строки. Если эта строка начинается с буквы "ж" в верхнем или нижнем регистре, 
программа выводит длину строки, а иначе выводится сообщение "Попробуйте снова". Используйте метод startsWith.

Sample Input 1:

жора

Sample Output 1:

4

Sample Input 2:

Жадина

Sample Output 2:

6

Sample Input 3:

Говядина

Sample Output 3:

Попробуйте снова

*/

let str = prompt();

if (str.startsWith("ж") || str.startsWith("Ж")) {
    console.log(str.length);
} else {
    console.log("Попробуйте снова");
}
