#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num, i;
    int *arr;
    
    scanf("%d", &num);
    arr = (int*) malloc(num * sizeof(int));
    
    for(i = num-1; i >= 0; i--)
        scanf("%d", arr + i);

    for(i = 0; i < num; i++)
        printf("%d ", *(arr + i));
    return 0;
}