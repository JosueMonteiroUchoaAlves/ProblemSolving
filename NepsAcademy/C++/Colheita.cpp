#include <bits/stdc++.h>
// Colheita

// https://neps.academy/br/exercise/2698

using namespace std;

// Os parenteses chamam o construtor do vetor, com: tamanho e elemento
int main()
{
    int l, c, maiorDiferenca = 0;
    cin >> l >> c;
    int matriz[l][c];

    for (int i = 0; i < l; i++){
        for (int j = 0; j < c; j++){
            cin >> matriz[i][j];
            if ( i > 0 ){ // não é a primeira linha
                if ((matriz[i][j] - matriz[i-1][j]) > maiorDiferenca){ // Diferença entre esse e o anterior de linha for a maior ate agora
                        maiorDiferenca  = matriz[i][j] - matriz[i-1][j];
                }
            }
            if  ( j > 0 ){ // não é a primeira coluna
                if ((matriz[i][j] - matriz[i][j-1]) > maiorDiferenca){ // Diferença entre esse e o anterior de coluna for a maior ate agora
                        maiorDiferenca  = matriz[i][j] - matriz[i][j-1];
                }
            }
            if ( i > 0 ){ // não é a primeira linha
                if (matriz[i][j] >= matriz[i-1][j]){
                        matriz[i][j] = matriz[i-1][j]; // a casa sera ocupada pelo menor item ate agora, e nao o item original
                }
            }
            if  ( j > 0 ){ // não é a primeira coluna

                if (matriz[i][j] >= matriz[i][j-1]){
                        matriz[i][j] = matriz[i][j-1]; // a casa sera ocupada pelo menor item ate agora, e nao o item original
                }
            }

        }
    }
    cout << maiorDiferenca;

    return 0;
}
