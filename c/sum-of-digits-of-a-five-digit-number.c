#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
	
    int n, res;
    scanf("%d", &n);
    
    res = n%10;
    
    while (n = n/10) {
        res += n%10;
    }
    
    printf("%d\n", res);
    
    return 0;
}