#include <stdio.h>
int main() {
  int a;
  double rad, pi = 3.1415926;
  scanf("%d",&a);

  rad = a*pi/180;
  printf("%.2lf\n",rad);

  return 0;
}
