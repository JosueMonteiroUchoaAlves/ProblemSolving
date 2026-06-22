// ========================
// Compilador online da OBI
// ========================

/*  100/100 pontos 
    realmente... era um erro bobo de logica
    testei com a questão "Taxi" do Codeforces, que é praticamente idêntica
*/

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
        total += g4; // cada grupo tem seu taxi

        restog2=g2%2; // resto = 1 se sobrar um par senao 0

        total += (int) (g2-restog2)/2 ;

        if (g1>g3){
            total += g3; // mesas com N3 completas...
            g1 -= g3; // porem vao sobrar alguns g1
        }else{
            // senao nao sobra g1 mesmo...
            total += g3; // entao vai ser literalmente os g3
            g1=0;
        }

        if(restog2==1){// se sobrou um par "folgado" 
            total += 1; // preenche uma mesa com o grupo g2 que faltou
            if(g1 != 0){ // e sobraram g1 tambem
                g1 -= 2; // tira 2 do g1 que podem sentar nela
            }
        }
        if (g1 > 0){ // se realmente nao tinha espaco pra todo mundo que faltou do g1
            restog1= g1%4; // vejo se vai sobrar gente

            total+=(g1-restog1)/4; // todos os g1 - os que nao completam a mesa

            if(restog1!=0){ 
                total+=1; // ponho a mesa dos que nao tinham completado a mesa
            }
        }
            cout << total << '\n';
    }
    return 0;
}
