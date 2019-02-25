#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int T;
    unsigned int number;
    unsigned int mask = -1;
    
    scanf("%d", &T);
    
    for (int i = 0; i < T; i++) {
        scanf("%u", &number);
        printf("%u\n", number^mask);
    }

    return 0;
}
