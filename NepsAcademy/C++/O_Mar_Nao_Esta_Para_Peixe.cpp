#include <bits/stdc++.h>
// 530 - O Mar não está para Peixe
// https://neps.academy/br/exercise/530

using namespace std;

int main(){
    const int tamanhoMar = 100;
    int n, Xi, Xf, Yi, Yf, casasMarcadas=0;
    cin >> n;
    vector<vector<int>> matriz(tamanhoMar, vector<int>(tamanhoMar, 0));


    for (int k =0; k< n; k++){
        cin >> Xi >> Xf >> Yi >> Yf;

        for (int i=Yi ; i<Yf ; i++){
            for(int j=Xi ; j<Xf ; j++){
                if(matriz[i][j] == 0){
                    casasMarcadas += 1;
                    matriz[i][j] = 1;
                }
            }
        }
    }
    cout << casasMarcadas << endl;
    return 0;
}
