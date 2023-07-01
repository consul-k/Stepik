#include <stdio.h>
int main(void){
  int rub;
  scanf("%d",&rub);

  double kurs, dollars;
  scanf("%lf",&kurs);

  dollars = rub*kurs;
  printf("%lf\n", dollars);
  return 0;
}
