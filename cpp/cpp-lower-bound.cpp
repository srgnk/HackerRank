#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n, q;
    cin >> n;
    vector<int> v(n);
    
    for(int i = 0; i < n; i++)
        cin >> v[i];
    sort(v.begin(), v.end());
    
    cin >> q;
    for(int i = 0; i < q; i++) {
        vector<int>::iterator low;
        int num;
        cin >> num;
        low = lower_bound(v.begin(), v.end(), num);
        if (v[low - v.begin()] == num)
            cout << "Yes " << (low - v.begin()+1) << endl;
        else
            cout << "No " << (low - v.begin()+1) << endl;
    }
    
    return 0;
}
