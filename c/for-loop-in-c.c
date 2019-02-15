#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>



int main() 
{
    int a, b;
    const char *numbers[9] = {"one", "two", "three", "four", "five",
                              "six", "seven", "eight", "nine"};
    scanf("%d\n%d", &a, &b);
    
    for (int i = a; i <= b; i++) {
        if ((i > 0) && (i < 10))
            printf("%s\n", numbers[i-1]);
        else
            printf("%s\n", (i%2) ? "odd" : "even");
    }

    return 0;
}

