#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str) {
    int n = str.size();
    int i = 1;
    stringstream ss(str);
    vector<int> out;
    while (ss) {
        char ch;
        int num;
        ss >> num;
        out.push_back(num);
        ss >> ch;
    }
    return out;
}

int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }
    
    return 0;
}
