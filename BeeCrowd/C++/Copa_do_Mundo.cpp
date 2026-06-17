#include <bits/stdc++.h>

using namespace std;
// Que solução elegante meus amigos... 
int main(){
    queue<char> times({'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P'});
    int a, b;
    for (int i=0; i<15; i++){
        cin >> a >> b;
        if (a > b){
            times.push(times.front());
            times.pop();
            times.pop();
        }else{
            times.pop();
            times.push(times.front());
            times.pop();
        }
    }
    cout << times.front() << '\n';
    return 0;
}
// 1, 5, 7, 8, 9, 15
// 4, 6, 10, 11
// 1, 4, 5, 6, 7, 8, 9, 10, 11, 15
