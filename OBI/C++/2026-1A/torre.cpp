// ========================
// Compilador online da OBI
// ========================

// 0/100 pontos (não deu tempo de enviar a versão final, inclusive nem é essa...)

#include <bits/stdc++.h>
using namespace std;

int main() {
    // comandos para agilizar entrada/saída
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // Digite seu código aqui, por exemplo:
    // cout << "resposta" << endl;
    vector<vector<int>> torre(999999, vector<int>(4, 0));
    map<int, int> torreMap;
    vector<int> X1(4, 0), X2(4, 0);
    int N, l=0, c=0, X;
    cin >> N;
    cout << N<< '\n';
    do{
        // transformando em lista
        torre[l][3]=N%10;
        
        if (N >= 10){
            torre[l][2]=(int) (N%100)/10;
            if (N >= 100){
                torre[l][1]=(int) (N%1000)/100;
                if (N >= 1000){
                    torre[l][0]=(int) (N%10000)/1000;
                }   
            }
            //cout << torre[l][0] << torre[l][1]<< torre[l][2]<< torre[l][3]<< '\n';
        }
        X1=torre[l];
        sort(X1.begin(), X1.end());
        X2=X1;
        reverse(X2.begin(), X2.end());
        X = (X2[0]*1000 + X2[1]*100+ X2[2]*10+ X2[3]) - (X1[0]*1000 + X1[1]*100+ X1[2]*10+ X1[3] );
        //cout << X1[0];
        torreMap[X]++;
        cout << X << '\n';
        N=X;
    }while(torreMap[X] != 2);

    return 0;
}
