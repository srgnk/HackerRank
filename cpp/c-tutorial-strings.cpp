#include <iostream>
#include <string>
using namespace std;

int main() {
    string a, b, aa, bb;
    cin >> a;
    cin >> b;
    aa = a;
    bb = b;
    char buf = aa[0];
    aa[0] = bb[0];
    bb[0] = buf;
    
    cout << a.size() << " " << b.size() << endl;
    cout << a+b << endl;
    cout << aa << " " << bb << endl;
    
  
    return 0;
}
