#include <bits/stdc++.h>
// https://cses.fi/problemset/task/1068
using namespace std;

int main() {
    long N;
    cin >> N;
    cout << N << ' ';
    while (N != 1){
        if(N%2==0){
            N=N/2;
        }else{
            N=(N*3)+1;
        }
         cout << N << ' ';
    }
    cout << '\n';
    return 0;
}
