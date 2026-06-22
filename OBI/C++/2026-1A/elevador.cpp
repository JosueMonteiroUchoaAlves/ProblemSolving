// ========================
// Compilador online da OBI
// ========================

// 100/100 pontos

#include <bits/stdc++.h>
using namespace std;

int main() {
    // comandos para agilizar entrada/saída
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // Digite seu código aqui, por exemplo:
    // cout << "resposta" << endl;

    int N, andar, tempo=0, Uandar;
    cin >> N;
    cin >> Uandar;
    for(int i=0; i<N-1; i++){
        cin >> andar;
        tempo += abs(andar-Uandar);
        Uandar=andar;
    }
    cout << tempo << '\n';

    return 0;
}
