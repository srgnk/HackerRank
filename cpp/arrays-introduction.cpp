#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int size;   //size variable for size of array
    int array[1001];
    cin >> size;
    for (int index = size; index; index--)
        cin >> array[index];
    for (int index = 1; index <= size; index++)
        cout << array[index] << " ";
    return 0;
}
