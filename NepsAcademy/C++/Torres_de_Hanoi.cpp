#include <bits/stdc++.h>
// Torres de Hanói

// https://neps.academy/br/exercise/337

using namespace std;

int Hanoi(int N, int orig, int dest, int temp, int profundidade){
    profundidade++;
    if (N == 1){
        orig = 0;
        dest = 1;
    }
    else{
        profundidade = Hanoi(N-1, orig, temp, dest, profundidade);
        dest = N;
        profundidade = Hanoi(N-1, temp, dest, orig, profundidade);
    }
    return profundidade;
}

int main()
{
    int N = 1, resultado, i = 0;

    while (N){
        i++;
        cin >> N;
        if (!N){
            break;
        }
        resultado = Hanoi(N, 1, 0, 0, 0);
        cout << "Teste " << i << endl << resultado << endl << endl;
    }

    return 0;
}
