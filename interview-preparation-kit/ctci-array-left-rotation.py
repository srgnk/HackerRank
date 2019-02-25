#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main() {
    int n; 
    int k; 
    
    scanf("%d %d",&n,&k);
    
    int *a = malloc(sizeof(int) * n);
    int *a_out = malloc(sizeof(int) * n);
    
    for(int a_i = 0; a_i < n; a_i++){
       scanf("%d",&a[a_i]);
    }
/*    
    for(int i = 0; i < k; i++){
        int buf = a[0];
        
        for (int j = 0; j < n-1; j++) {
            a[j] = a[j+1];
        }
            
        a[n-1] = buf;
    }
*/    
    for (int i = 0; i < n; i++) {
        a_out[(i+n-k)%n] = a[i];
    }
    for(int a_i = 0; a_i < n; a_i++){
       printf("%d ", a_out[a_i]);
    }   
    printf("\n");
    
    free(a);
    return 0;
}
