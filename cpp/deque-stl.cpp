#include <iostream>
#include <deque> 
#include <algorithm>
using namespace std;

void printKMax(int arr[], int n, int k) {
    std::deque<int>  dq(k);
    int i;
    
    for (i = 0; i < k; ++i) {
        while ( (!dq.empty()) && arr[i] >= arr[dq.back()])
            dq.pop_back();
 
        dq.push_back(i);
    }
 
    for ( ; i < n; ++i) {
        cout << arr[dq.front()] << " ";
 
        while ( (!dq.empty()) && dq.front() <= i - k)
            dq.pop_front();
 
        while ( (!dq.empty()) && arr[i] >= arr[dq.back()])
            dq.pop_back();
 
        dq.push_back(i);
    }
 
    cout << arr[dq.front()] << endl;
}

int main(){
  
   int t;
   cin >> t;
   while(t>0) {
      int n,k;
       cin >> n >> k;
       int i;
       int arr[n];
       for(i=0;i<n;i++)
            cin >> arr[i];
       printKMax(arr, n, k);
       t--;
     }
     return 0;
}
