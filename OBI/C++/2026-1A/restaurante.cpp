// ========================
// Compilador online da OBI
// ========================

// 60/100 pontos (mas acho que já sei porque...)

#include <bits/stdc++.h>
using namespace std;

int main() {
    // comandos para agilizar entrada/saída
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // Digite seu código aqui, por exemplo:
    // cout << "resposta" << endl;

    int total=0, g1, g2,g3,g4, restog2=0, restog1;
    cin >> g1>> g2>> g3 >> g4;

    //subtarefa 2
    if (g2 == 0 && g3 == 0 && g4 == 0){
        restog1= g1%4;
        if(restog1!=0){
            total+=1;
        }
        total+=(g1-restog1)/4;
        cout << total << '\n';
    }
    else{
        total += g4;
        // divide por 2 e arredonda
        restog2=g2%2; // se sobrar um par
        total += (int) (g2-restog2)/2 ;
        if (g1>g3){
            total += g3; // mesas com N3 completas, porem sobraram g1
            g1 -= g3;
            if(restog2==1){// so pode ser 1 par
                    total += 1; // preenche a mesa com o grupo g2 que faltou
                    g1 -= 2; // tira 2 do g1 que podem sentar nela
            }
            if (g1 > 0){ // se realmente nao tinha espaco pra todo mundo que falou do g1
                restog1= g1%4;
                if(restog1!=0){
                    total+=1;
                }
                total+=(g1-restog1)/4;
            }

        }
        else{
            total += g3;
        }
            cout << total << '\n';
    }
    return 0;
}
