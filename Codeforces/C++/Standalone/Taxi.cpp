#include <bits/stdc++.h>

using namespace std;
// contest/158 - B. Taxi
// https://codeforces.com/contest/158
//
int main() {
    // comandos para agilizar entrada/saída
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    /*=============================*/

    int N, G, total=0, g1=0, g2=0,g3=0,g4=0, restog2=0, restog1=0;
    
    cin >> N;
    for(int i=0; i<N;i++){
        cin >> G;
        switch(G){
            case 1: g1++; break;
            case 2: g2++; break;
            case 3: g3++; break;
            case 4: g4++; break;
        }
    }
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

    return 0;
}
