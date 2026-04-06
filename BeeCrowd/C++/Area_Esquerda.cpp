#include <bits/stdc++.h>
// 1189 - Área Esquerda
// https://judge.beecrowd.com/pt/problems/view/1189

using namespace std;

int main(){
    char op=' ';
    cin >> op;
    int counter=0;
    double elem=0, elemSum=0;

    for(int i=0; i<12 ; i++){
        for(int j=0; j<12; j++){
            cin >> elem;
            if(j<5){
                if((i>j) && (i+j+2<12+1)){
                    counter++;
                    elemSum+=elem;
                }
            }
        }
    }
    if(op=='S'){
        cout << fixed << setprecision(1) << elemSum << endl;
    }else{
        cout << fixed << setprecision(1) << elemSum/counter << endl;
    }

    return 0;
}
/*
1 1 1 1 1 1 1 1 1 1 1 1
2 1 1 1 1 1 1 1 1 1 1 1
2 2 1 1 1 1 1 1 1 1 1 1
2 2 2 1 1 1 1 1 1 1 1 1
2 2 2 2 1 1 1 1 1 1 1 1
2 2 2 2 2 1 1 1 1 1 1 1
2 2 2 2 2 1 1 1 1 1 1 1
2 2 2 2 1 1 1 1 1 1 1 1
2 2 2 1 1 1 1 1 1 1 1 1
2 2 1 1 1 1 1 1 1 1 1 1
2 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1
*/
