#include <bits/stdc++.h>
// 1187 - Área Superior
// https://judge.beecrowd.com/pt/problems/view/1187

using namespace std;

int main(){
    char op = ' ';
    cin >> op;
    int totalElem=0;
    // A falta de precisão de usar o float no lugar do double me deu uma dor de cabeça!
    // Pois a lógica estava correta, mas a falta de precisão do float fazia minha resposta sair "levemente" errada!
    double sumElem=0, num=0;
    for (int i = 0; i< 12; i++){
        for ( int j = 0; j< 12; j++){
            cin >> num;

            if (i < 5 ){ // antes da metade da lista
                // J > I (1 endexed) é a parte superior da diagonal principal
                // Um numero é da diagonal secundaria se I + J == N + 1, e queremos os numeros que vem antes dela...
                if ((j >= i+1) && (i + j + 2 < 12 + 1)){
                    totalElem++;
                    sumElem += num;
                }
            }
        }
        cout << totalElem << endl;
    }
    if (op == 'S'){
        cout << fixed << setprecision(1) << sumElem << endl;
    }
    else{
        cout << fixed << setprecision(1) << sumElem/totalElem << endl;
    }
    return 0;
}
/*
    1 2 2 2 2 2 2 2 2 2 2 1

    1 1 2 2 2 2 2 2 2 2 1 1

    1 1 1 2 2 2 2 2 2 1 1 1

    1 1 1 1 2 2 2 2 1 1 1 1

    1 1 1 1 1 2 2 1 1 1 1 1

    1 1 1 1 1 1 1 1 1 1 1 1

    1 1 1 1 1 1 1 1 1 1 1 1

    1 1 1 1 1 1 1 1 1 1 1 1

    1 1 1 1 1 1 1 1 1 1 1 1

    1 1 1 1 1 1 1 1 1 1 1 1

    1 1 1 1 1 1 1 1 1 1 1 1

    1 1 1 1 1 1 1 1 1 1 1 1

*/
