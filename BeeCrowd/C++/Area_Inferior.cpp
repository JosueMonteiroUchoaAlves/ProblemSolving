#include <bits/stdc++.h>
// Área Inferior
// https://judge.beecrowd.com/pt/problems/view/1188

using namespace std;

int main(){
    char op = ' ';
    cin >> op;
    int totalCount=0;
    double totalSum=0, elem=0;

    for(int i=0;i<12;i++){
        for(int j=0; j<12; j++){
            cin >> elem;
            if (i > 6){
                if ((i + j + 2 > 12 + 1) && (j < i)){
                    totalCount++;
                    totalSum += elem;
                }
            }
        }
    }
    if(op=='S'){
        cout << fixed << setprecision(1) << totalSum << endl;
    }
    else{
        cout << fixed << setprecision(1) << totalSum/totalCount << endl;
    }
    return 0;
}
/*
1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 2 2 1 1 1 1 1
1 1 1 1 2 2 2 2 1 1 1 1
1 1 1 2 2 2 2 2 2 1 1 1
1 1 2 2 2 2 2 2 2 2 1 1
1 2 2 2 2 2 2 2 2 2 2 1
*/
