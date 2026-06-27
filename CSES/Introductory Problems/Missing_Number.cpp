#include <bits/stdc++.h>
// https://cses.fi/problemset/model/1083/
using namespace std;

int main() {
    int N, n;
    set<int> numbers;
    cin >> N;

    for (int i=0;i<N-1;i++){
        cin >> n;
        numbers.insert(n);
    }
    for (int i=1;i<=N;i++){
        if(numbers.find(i) == numbers.end()){
            cout << i << '\n';
            break;
        }
    }
    return 0;
}
