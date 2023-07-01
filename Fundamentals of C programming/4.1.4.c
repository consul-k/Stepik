#include <stdio.h>
int main() {
  int a, b;
  double c, summa;
  scanf("%d",&a);
  scanf("%d",&b);
  scanf("%lf",&c);

  summa = (b-a)*c;
  printf("%.2lf\n",summa);

  return 0;
}
