#include <stdio.h>
#include <math.h>
int main() {
  double a, b, y, pi = 3.141593, s;
  scanf("%lf",&a);
  scanf("%lf",&b);
  scanf("%lf",&y);
  y = sin((y * pi)/180);
  s = 0.5*a*b*y;
  printf("%.2lf\n",s);
  return 0;
}
