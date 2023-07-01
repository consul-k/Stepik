#include <stdio.h>
#include <math.h>
int main() {
  double x1, y1, x2, y2, l;
  scanf("%lf",&x1);
  scanf("%lf",&y1);
  scanf("%lf",&x2);
  scanf("%lf",&y2);

  l = pow((fabs(x1-x2)),2)+pow((fabs(y1-y2)),2);
  printf("%.2lf\n",sqrt(l));

  return 0;
}
