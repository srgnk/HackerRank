#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

#define min(a, b) ((a) < (b) ? (a) : (b))
#define max(a, b) ((a) < (b) ? (b) : (a))

int main() 
{
    int n;
    scanf("%d", &n);
    
    for (int i = 0; i < 2*n - 1; i++) {
        int lead = 0;
        int lower_bound;
        
        if (i < n)
            lower_bound = n - i;
        else
            lower_bound = 2 + i%n;
        
        for (int j = 0; j < 2*n - 1; j++) {
            if (j < n-1) {
                printf("%d ", max(lower_bound, n - lead));
                lead++;
            }
            else {
                printf("%d ", max(lower_bound, n - lead));
                lead--;
            }
        }
        printf("\n");
    }
    
    return 0;
}