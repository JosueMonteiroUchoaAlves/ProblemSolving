#include <bits/stdc++.h>
// Lâmpadas

// https://neps.academy/br/exercise/52

using namespace std;

// Os parenteses chamam o construtor do vetor, com: tamanho e elemento
int main()
{
    int n, a = 0, b = 0, x;
    cin >> n;
    for (int i = 0; i < n; i++){
        cin >> x;
        if( x == 1){
            a = a ^ 1;
        }
        else{
            a = a ^ 1;
            b = b ^ 1;
        }
    }
    cout << a << endl <<  b;

    return 0;
}
