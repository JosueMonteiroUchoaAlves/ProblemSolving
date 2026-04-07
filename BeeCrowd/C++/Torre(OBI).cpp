#include <bits/stdc++.h>
// 45 - Torre (OBI 2015)
// https://neps.academy/br/exercise/45

using namespace std;

int main(){
    int n, maiorCruzamentoAtual=0;
    cin >> n;

    vector<int> sumLinha(n, 0); //  Elemento I corresponde a linha I
    /* 
    -1 porque a soma da linha/coluna pode ser 0 e se for nao quero que 
    meu IF me faça somar aquela linha denovo
    */
    vector<int> sumColuna(n, 0); //  Elemento J corresponde a linha J

    vector<vector<int>> matriz(n, vector<int>(n, 0));

    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            cin >> matriz[i][j];
        }
    }
    /*
    Ao invés de me perguntar toda vez se 
    aquela linha ou coluna foi calculada,vou calcular todas logo!
    Pois independente de qualquer coisa essa "passada" pela matriz para
    fazer o calculo teria que acontecer. Vai sair mais barato do que aqueles
    IFs se repetindo 1milhao de vezes.
    */ 
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            sumLinha[i] += matriz [i][j];
            sumColuna[j] += matriz [i][j]; 
        }
    }

    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            if (sumLinha[i] + sumColuna[j] - (matriz[i][j] * 2) > maiorCruzamentoAtual){
                maiorCruzamentoAtual = sumLinha[i] + sumColuna[j] - (matriz[i][j] * 2);
            }
        }
    }
    
    cout << maiorCruzamentoAtual << endl;
    return 0;
}
