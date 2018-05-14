#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;


int main() {
    int q;
    cin >> q;
    set<int> s;
    
    for (int i = 0; i < q; i++) {
        int type, num;
        cin >> type >> num;
        
        switch(type) {
            case 1:
                s.insert(num);
                break;
            case 2:
                s.erase(num);
                break;
            case 3:
                if (s.find(num) == s.end())
                    cout << "No" << endl;
                else
                    cout << "Yes" << endl;
                break;
        }
    }
    return 0;
}
