#include <bits/stdc++.h>

using namespace std;

/*
Eu estava tendo problema com a precisao ao comparar os resultados, e aprendi isso:
A Margem Epsilon :
    Nunca devo utilizar "==" para comparar números de ponto flutuante.
    Devo verificar se a distância absoluta entre os dois números é menor 
    que uma margem de erro minúscula, conhecida como Epsilon. Para problemas da
    OBI que pedem 4 casas decimais de precisão, um Epsilon de 1e-5 (0.00001) é o ideal, por exemplo.
*/


//recebe o tamanho do teste em que eu estou agora e retorna a area do corte
long double areaValue(vector<int>& tiras, int N, long double corte, int lowerbound){
    long double totalSize=0;
    for(int i=lowerbound; i<N; i++){
        totalSize+=tiras[i]-corte; 
    } 
    return totalSize;
}

int main(){
    ios_base::sync_with_stdio(false);

    int N;
    double A;
    while (cin >> N >> A && !(N == 0 && A == 0)){
        vector<int> tiras(N);
        int somaAreaTotal=0;
        for (auto& t: tiras) {
            cin >> t;
            somaAreaTotal+=t; 
        }
        sort(tiras.begin(), tiras.end());

        //se tiver com a area certa logo de cara
        if (somaAreaTotal == A){
            cout << ":D\n";
            continue;
        }

        long double l=0.0, r=tiras[N-1], mid, areaCortada=0;
        int tentativas = 0;
        while(l<=r && tentativas <= 60){
            mid=(l+r)/2;
            tentativas++;
            //iterador do menor item que seja maior ou igual a altura em que eu quero cortar
            auto it=lower_bound(tiras.begin(), tiras.end(), mid); 
            int menorQueSeraCortado = it-tiras.begin(); // ja vem 0-indexed
            areaCortada=areaValue(tiras, N, mid, menorQueSeraCortado);

            // a distancia absoluta entre o que quero e o que tenho é minima?
            if (abs(areaCortada - A) <= 1e-5){
                break;
            }

            if(areaCortada>A){ // cortou muito
                l=mid;
            }
            if(areaCortada<A){
                r=mid;
            }
        }

        if (abs(areaCortada - A) <= 1e-5){
            cout << fixed << setprecision(4) << mid << '\n';
        }else{
            cout << "-.-"  << '\n';
        }
    }
    return 0;
}

