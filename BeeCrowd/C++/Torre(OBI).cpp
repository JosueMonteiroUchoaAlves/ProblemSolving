#include <bits/stdc++.h>
// 45 - Torre (OBI 2015)
// https://neps.academy/br/exercise/45

using namespace std;

int SomarLinha(vector<int> linha){
    return accumulate(linha.begin(), linha.end(), 0);
}

int main(){
    int n, maiorCruzamentoAtual=0;
    cin >> n;

    vector<int> sumLinha(n, -1); //  Elemento I corresponde a linha I
    /* 
    -1 porque a soma da linha/coluna pode ser 0 e se for nao quero que 
    meu IF me faça somar aquela linha denovo
    */
    vector<int> sumColuna(n, -1); //  Elemento J corresponde a linha J

    vector<vector<int>> matriz(n, vector<int>(n, 0));

    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            cin >> matriz[i][j];
        }
    }

    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            if (sumLinha[i] == -1){
                sumLinha[i] = SomarLinha(matriz[i]);
            }
            if (sumColuna[j] == -1){
                sumColuna[j] += 1;
                for (int i=0; i<n; i++){
                    sumColuna[j] += matriz[i][j];
                }
            }
            if (sumLinha[i] + sumColuna[j] - (matriz[i][j] * 2) > maiorCruzamentoAtual){
                maiorCruzamentoAtual = sumLinha[i] + sumColuna[j] - (matriz[i][j] * 2);
            }
        }
    }
    
    cout << maiorCruzamentoAtual << endl;
    return 0;
}
