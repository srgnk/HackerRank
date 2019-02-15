#include <stdio.h>
#include <math.h>

void update(int *a, int *b) {
    int buf = *a;
    
    *a = *a + *b;
    *b = abs(buf - *b);
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}