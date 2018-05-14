#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int start, end;
    const string Digits[] = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    cin >> start;
    cin >> end;
    
    for (int i = start; i <= end; i++) {
        if (i > 9) {
            if (i%2)
                cout << "odd" << endl;
            else
                cout << "even" << endl;
            continue;
        }
        cout << Digits[i] << endl;
    }
        
    return 0;
}
