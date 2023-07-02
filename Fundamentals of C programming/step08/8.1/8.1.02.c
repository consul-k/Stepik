/*

Палиндром
Определить является ли массив палиндромом, т.е. первый элемент равен последнему, второй предпоследнему и т.д.

Входные данные:
Первая строка число N,(N>0)N,(N>0) -- длина массива. Длина массива не более 100 элементов. Вторая строка NN  целых чисел, записанных через пробел

Выходные данные:
YES -- если массив является палиндромом, NO -- в противном случае.

Sample Input 1:

5
 10 -93 22 75 12

Sample Output 1:

NO

Sample Input 2:

4
1 2 2 1

Sample Output 2:

YES

*/

#include <stdio.h>

int main(void) {  
  int n=0,count=0,s=0,ans=0;
  int num[100] = {0};
  
  scanf("%d",&count);
 
  for(int i = 0; i <= count; i = i + 1){
    scanf("%d",&n);
    num[i] = num[i] + n;
  }

  for(int i = count-1; i >= 0; i = i - 1){
	if (num[i]!=num[s]) {
			ans++;
	    }
    s++;
  }

  if (ans==0)
  printf("YES");
  else
  printf("NO");

  return 0;
}
