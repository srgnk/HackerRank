#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

int main() {
    int q;
    cin >> q;
    map<string, int> m;
    
    for (int i = 0; i < q; i++) {
        int type, num;
        string name;
        cin >> type;
        
        switch(type) {
            case 1:
                cin >> name >> num;
                if (m.find(name) == m.end())
                    m.insert(make_pair(name, num));
                else
                    m[name] += num;
                break;
            case 2:
                cin >> name;
                m.erase(name);
                break;
            case 3:
                cin >> name;
                if (m.find(name) == m.end())
                    cout << "0" << endl;
                else
                    cout << m[name] << endl;
                break;
        }
    }
    return 0;
}