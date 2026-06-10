#include <bits/stdc++.h>

using namespace std;

int main(){
    int totalTerritory;
    cin >> totalTerritory;

    vector<int> territory(totalTerritory+10); // +10 por seguranca

    for (int i=1;i<=totalTerritory;i++){
        cin >> territory[i];
    }

    int somaInicio=0, somaFim=0;
    int counter=1, i=1, j=totalTerritory;
    somaInicio += territory[i];
    somaFim += territory[j];
    do{     
        if (somaInicio >= somaFim){
            j-=1;
            somaFim += territory[j];
        }else{
            i+=1;
            somaInicio += territory[i]; 
        }
        counter+=1;
    }while (counter < totalTerritory);
    cout << i << '\n';
    return 0;
}

