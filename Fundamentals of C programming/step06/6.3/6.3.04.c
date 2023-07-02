/*

Даны две точки: А(х1,у1)А(х1​,у1​) и В(х2,у2)В(х2​,у2​). Составить программу, определяющую, которая из точек находится ближе к началу координат.

Входные данные:
Четыре целых числа. Первые два числа -- координаты точки AA(первая точка), следующие два числа -- координаты точки BB(вторая точка).

Выходные данные:
Вывести одно число, номер точки, которая находится ближе к началу координат. Если расстояния между точками до начала координат равны - вывести 0.

Sample Input:

1 2
 1 -3

Sample Output:

1

*/

#include <stdio.h>
#include <math.h>

int main() {
  int x1,y1,x2,y2;
  double r1,r2;
  scanf("%d %d",&x1,&y1);
  scanf("%d %d",&x2,&y2);
    
  r1 = sqrt(pow(x1,2)+pow(y1,2));
  r2 = sqrt(pow(x2,2)+pow(y2,2));
  
  if (r1<r2) {
	printf("%d\n",1);
  } else 
	printf("%d\n",2);

    
  return 0;
}
