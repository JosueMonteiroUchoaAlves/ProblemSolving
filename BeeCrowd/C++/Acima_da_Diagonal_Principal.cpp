#include <bits/stdc++.h>
// 1183 - Acima da Diagonal Principal
// https://judge.beecrowd.com/pt/problems/view/1183
//
using namespace std;

int main(){
    float elem=0, res=0, totalElem=0;
    char op=' ';

    cin >> op;

    for (int i = 0; i< 12; i++){
        for (int j =0; j < 12; j++){
            cin >> elem;
            if(i >= j){ // se o indice de linha for maior ou igual ao de coluna, não é a parte superior da matriz!
                continue;
            }
            else{
                res += elem;
                totalElem +=1;
            }
        }
    }
    if( op == 'S'){
        // fixed: Garante que o número será impresso em notação decimal padrão (não em notação científica). E o setprecision(1): Crava as casas decimais em 1.
        cout << fixed << setprecision(1) << res << endl;
    }
    else{
        cout << fixed << setprecision(1) << res/totalElem << endl;
    }

    return 0;
}
