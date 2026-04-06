#include <bits/stdc++.h>
// 1186 - Abaixo da Diagonal Secundária 
// https://judge.beecrowd.com/pt/problems/view/1186
//
using namespace std;

int main(){
    char op = ' ';
    float elem=0, res=0;
    int totalElem=0;
    cin >> op;
    for (int i = 0; i < 12; i++){
        for (int j = 0; j < 12; j++){
            cin >> elem;
            if (i + j + 2 > 13 ){ // maior que N + 1
                res += elem;
                totalElem ++;
            }
        }
    }
    if (op == 'S'){
        cout << fixed << setprecision(1) << res << endl;
    }
    else{
        cout << fixed << setprecision(1) << res/totalElem << endl;
    }
    return 0;
}
