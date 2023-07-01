#include <stdio.h>
#include <math.h>
int main(void){
  double a, b, c, d, e, f, h;
  double res;
  scanf("%lf",&a);
  scanf("%lf",&b);
  scanf("%lf",&c);
  scanf("%lf",&d);
  scanf("%lf",&e);
  scanf("%lf",&f);
  scanf("%lf",&h);

  res = (double)(a/(b*(c/(d*(e/(f*h))))));  
  printf("%.2lf", res);

  return 0;
}
