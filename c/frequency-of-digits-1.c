#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int freq[10];
    char string[1000];
    
    scanf("%s", &string);
    
    for (int i = 0; i < 10; i++)
        freq[i] = 0;
    
    for (int i = 0; i < strlen(string); i++) {
        int pos = string[i] - '0';
        if (pos >= 0 && pos < 10)
            freq[pos]++;
    }
    
    for (int i = 0; i < 10; i++)
        printf("%d ", freq[i]);

    return 0;
}
