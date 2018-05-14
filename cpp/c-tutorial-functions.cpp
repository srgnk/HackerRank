#include <iostream>
#include <cstdio>
using namespace std;


int max_of_four(int a, int b, int c, int d) {
    int ret = a;
    if (b > ret)
        ret = b;
    if (c > ret)
        ret = c;
    if (d > ret)
        ret = d;
    return ret;
}


int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}

