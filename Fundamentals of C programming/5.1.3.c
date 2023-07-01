/*

Идёт kk секунда суток. Определить, сколько целых часов и целых минут будут показывать электронные часы, если на 0-ой секунде они показывают 0 0.

Sample Input:

34961

Sample Output:

9 42

*/

#include <stdio.h>

int main() {
  int k, h, m;
  scanf("%d",&k);
  h = k / 60 /60;
  m = k / 60 % 60;
  printf("%d %d",h,m);
  return 0;
}
