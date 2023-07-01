#include <stdio.h>
int main() {
  int a, number;
  scanf("%d",&a);

  number = (a+1)%2;
  printf("%d\n",number);

  return 0;
}
