#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int N;
    int array[1010];
    cin >> N;
    for (int i = N; i; i--)
        cin >> array[i];
    for (int i = 1; i <= N; i++)
        cout << array[i] << " ";
    return 0;
}
