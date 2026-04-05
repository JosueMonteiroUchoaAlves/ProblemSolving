#include <bits/stdc++.h>

// Quadrado Mágico (OBI 2007)

// https://neps.academy/br/exercise/236

using namespace std;

int main()
{
    int n, elem;

    cin >> n;

    //Somas
    int SumMainDiag=0, SumAuxDiag=0;

    vector<int> SumLin(n,0), SumCol(n,0); // vector<tipo> nome(tamanhoInicial, valoresIniciais)

    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            cin >> elem;
            if (i == j){ // Os elementos da diagonal principal possuem os indices I e J iguais
                SumMainDiag += elem;
            }
            if ((i + j + 2)  == (n + 1))    { // Se i + 1 + j + 1 (estou corrigindo para 1-indexed) for igual a N + 1, então faz parte da diagonal auxiliar.
                SumAuxDiag += elem;
            }
            SumLin[i] += elem;
            SumCol[j] += elem;
        }
    }

    if ((count(SumLin.begin(), SumLin.end(), SumLin[0]) == SumLin.size()) && (count(SumCol.begin(), SumCol.end(), SumCol[0]) == SumCol.size()) && (SumLin[0] == SumCol[0]) && (SumMainDiag == SumAuxDiag) && (SumMainDiag == SumLin[0])){
        cout << SumMainDiag;
    }else{
        cout << -1;
    }

    return 0;
}
