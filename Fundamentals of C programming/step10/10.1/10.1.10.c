/*

Переделайте функцию, написанную в прошлом уроке, таким образом, чтобы она возвращала число 1, если число KK простое, или 0, если число KK составное.

Sample Input 1:

8

Sample Output 1:

0

Sample Input 2:

2

Sample Output 2:

1

*/

int is_prime(int k){
    int i,a=0;
    for(i = 1; i<=k; i++)
      if(k%i==0)
        a++;
      if (a>2)
          return 0;
      if (a<=2)
        return 1;  
}
