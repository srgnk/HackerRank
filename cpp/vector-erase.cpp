#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n, pos, right, left;
    cin >> n;
    vector<int> vec(n);
    
    for (int i = 0; i < n; i++)
        cin >> vec[i];
    
    cin >> pos;
    cin >> left >> right;
    vec.erase(vec.begin() + pos - 1);
    vec.erase(vec.begin() + left - 1, vec.begin() + right - 1);
    
    cout << vec.size() << endl;
    for (int i = 0; i < vec.size(); i++)
        cout << vec[i] << " ";
    
    return 0;
}
