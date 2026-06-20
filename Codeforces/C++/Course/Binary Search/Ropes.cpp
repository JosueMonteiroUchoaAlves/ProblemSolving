#include <bits/stdc++.h>

using namespace std;

/*
    Pensamentos iniciais:
        - pode sobrar pedaços de peças, então podem sobrar peças, mas 
          talvez seria um disperdiço de material...
        - o tamanho minimo é 0: nao cortei nada e ja tenho K peças de tamanho maximo;
        - o tamanho máximo vai ser o tamanho da maior peça, pois posso nem tocar na menor e
          com as maiores ja ter K peças de tamanho maximo
        
        - se eu cortei em pedacos de tamanho P e deu mais que K peças, então tem 
          como cortar pedacos maiores
        - se eu cortei em pedacos de tamanho P e deu menos que K pecas, entao os
          pedacos estao grandes demais! tenho que cortar menos
        - se deram K peças, eu corto mais porque pode ter sobrado um espacinho que eu possa utilizar
*/

int pedacos(vector<double>& tiras, double corte){
    int contador=0;
    for(double& t:tiras){
        contador+= (int) t/corte;
    }
    return contador;
}

int main(){
    ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);

    /*=============================*/
    int N, K;
    double big=-1;

    cin >> N >> K;
    vector<double> ropes(N);

    for (double& r:ropes){
        cin >> r;
        big = (r>big) ? r:big;
    }
    double left=0.0, right=big, mid;
    int p;
    for (int i=0; i<100; i++){
        mid = (left+right)/2;

        p=pedacos(ropes, mid);
        //cout <<"foram "<< p << " pedacos de " << mid << '\n';
        if (p == K){
            left=mid;
        }
        if (p < K){
            right=mid;
        }
        if (p > K){
            left=mid;
        }
    }
    cout << fixed << setprecision(6) << mid << '\n';

    return 0;
}

