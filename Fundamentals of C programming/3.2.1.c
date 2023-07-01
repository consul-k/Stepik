#include <stdio.h> 
int main(void) {
  int a, b, res;

  scanf("%d",&a);
  scanf("%d",&b);

  res = a + b;

  int c;

  scanf("%d",&c);
  res = res - c;

  printf("%d\n", res);
  return 0;
}
