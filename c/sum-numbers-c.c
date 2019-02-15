#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    int int1, int2;
    float fl1, fl2;
    scanf("%d %d", &int1, &int2);
    scanf("%f %f", &fl1, &fl2);
	
    printf("%d %d\n", int1 + int2, int1 - int2);
    printf("%.1f %.1f\n", fl1 + fl2, fl1 - fl2);
    return 0;
}