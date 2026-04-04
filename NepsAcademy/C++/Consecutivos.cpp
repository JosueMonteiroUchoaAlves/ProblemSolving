#include <bits/stdc++.h>
// Consecutivos

// https://neps.academy/br/exercise/110

using namespace std;

int main()
{
    int n, valor, passado, maiorSeq=0, seq=0;

    cin >> n;


    for (int i = 0; i < n; i++){
        cin >> valor;

        if (i == 0){
            passado = valor;
        }

        if (valor == passado){
            seq++;
        }else{
            seq=1;
        }

        if(seq > maiorSeq){
            maiorSeq = seq;
        }
        passado = valor;

    }
    cout << maiorSeq;

    return 0;
}
