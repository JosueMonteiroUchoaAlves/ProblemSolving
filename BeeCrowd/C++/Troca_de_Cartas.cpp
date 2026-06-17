#include <bits/stdc++.h>

using namespace std;

int main(){
    int Na, Nb, a, b;
    while (cin >> Na >> Nb && !(Na == 0 && Nb == 0)){
        // As cartas podem ser unicas, ja que só de ter 1 carta daquela ela ja nao vai querer outra
        set<int> A, B;
        int AemB=0, BemA=0; // zera a cada par de conjuntos de cartas

        for (int i=0; i<Na; i++){
            cin >> a;
            A.insert(a);
        }
        for (int i=0; i<Nb; i++){
            cin >> b;
            B.insert(b);
        }
        // conto quantas cartas unicas de Alice a Beatriz ja tem
        for (auto& c: A){
            if (!B.count(c)){
                AemB++;
            }
        }
        // conto quantas cartas unicas de Beatriz a Alice ja tem
        for (auto& c: B){
            if (!A.count(c)){
                BemA++;
            }
        }
        /*
            No final das contas, vi quantas cartas de Alice a Beatriz não tem, e quantas
            cartas de Alice a Beatriz não tem.Então as cartas que elas tem em comum nao podem
            ser trocadas, o que obedece às duas regras: sem trocas de cartas iguais, e sem
            receber cartas repetidas, já que as iguais sao ignoradas.
             Pego o menor numero e digo que este é a quantidade de pares que podem ser formados.
        */
        cout << min(AemB, BemA) << '\n';

    }
    return 0;
}
// 1, 5, 7, 8, 9, 15
// 4, 6, 10, 11
// 1, 4, 5, 6, 7, 8, 9, 10, 11, 15
