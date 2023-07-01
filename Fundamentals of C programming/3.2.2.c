#include <stdio.h>
int main(void){

  int h; // часы
  int m; // минуты
  int s; // секунды

  scanf("%d",&h);
  scanf("%d",&m);
  scanf("%d",&s);

  int seconds = h*60*60 + m*60 + s;

  printf("%d\n", seconds);

  return 0;
}
