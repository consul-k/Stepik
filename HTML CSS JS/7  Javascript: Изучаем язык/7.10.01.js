/*

  На вход подаётся число.

    Выведите YES, если число (чётное и двузначное) или нечётное трёхзначное, иначе выведите NO.

Sample Input 1:

42

Sample Output 1:

YES

Sample Input 2:

79

Sample Output 2:

NO

Sample Input 3:

789

Sample Output 3:

YES

*/

let num = Number(prompt());
if((num%2!=1 && num>9 && num<100)||(num%2==1 && num>99 && num < 1000))
    console.log('YES');
else
    console.log('NO');
