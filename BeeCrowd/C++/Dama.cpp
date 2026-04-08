#include <bits/stdc++.h>
// 1087 - Dama (Maratona de Programação da SBC - 2008)
// https://judge.beecrowd.com/pt/problems/view/1087

using namespace std;

int main(){
    int x1,y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;

    while ( x1 != 0 ){
        x2 = abs(x2 - x1);
        y2 = abs(y2 - y1); // Distancia entre fim e inicio

        if (x2 == 0 && y2 == 0){
            cout << 0 << endl;
        }
        else if ( x2 == y2){
            cout << 1 << endl;
        }
        else if ( x2 == 0 || y2 == 0){
            cout << 1 << endl;
        }
        else{
            cout << 2 << endl;
        }
        cin >> x1 >> y1 >> x2 >> y2;
    }

    return 0;
}
