#include <stdio.h>
#include <math.h>
int main() {
  double a, b, c, p, s;
  scanf("%lf",&a);
  scanf("%lf",&b);
  scanf("%lf",&c);
  p = (a+b+c)/2;
  s = sqrt(p*(p-a)*(p-b)*(p-c));
  printf("%.2lf\n",s);
  return 0;
}
