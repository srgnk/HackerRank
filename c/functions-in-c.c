#include <stdio.h>

int max_of_four(int a, int b, int c, int d)
{
    int res = a;
    
    if (b > res)
        res = b;
    if (c > res)
        res = c;
    if (d > res)
        res = d;
    
    return res;
}


int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}