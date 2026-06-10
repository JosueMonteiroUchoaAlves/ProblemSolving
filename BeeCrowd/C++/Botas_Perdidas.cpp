#include <bits/stdc++.h>

using namespace std;

int main(){
    const int TAM_MAX_BOTA = 70;
    vector<int> botas(TAM_MAX_BOTA, 0);
    int paresFormados=0, N;
    int i;
    int bota, botasAntes;
    char pe;
    while (cin >> N){
        for (i=0; i<N; i++){
            cin >> bota >> pe;
            
            botasAntes = abs(botas[bota]);
            if (pe == 'D'){
                botas[bota] += 1;
            }
            else{
                botas[bota] -= 1;
            }
            if (botasAntes > abs(botas[bota])){ // diminuiu numero de botas (seja pe direito ou esquerdo)
                paresFormados += 1;
            }
        }
        cout << paresFormados << '\n';
        paresFormados=0;
        //zerando vetor
        fill(botas.begin(), botas.end(), 0);
    }


    return 0;
}

