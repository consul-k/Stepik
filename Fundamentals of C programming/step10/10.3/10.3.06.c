/*

Написать функцию int gcd(int x, int y), которая ищет наибольший общий делитель для чисел x и y.

Sample Input:

14 49

Sample Output:

7

*/

int gcd(int x, int y){
  while (x&&y)
        if (x >= y)      
          x=x% y;  
        else
          y =y% x;
    return x | y;
}
