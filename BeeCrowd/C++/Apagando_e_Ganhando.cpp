#include <bits/stdc++.h>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);

    /*=============================*/
    int N, D;

    while (cin >> N >> D && (N != 0 && D != 0)){
        vector<int> digitos; // que vai funcionar como uma pilha  
        string numero;
        int digito;
        int apagados=0;
        cin >> numero;
        for (int i=0; i<N; i++){
            digito = numero[i]-'0'; // se fossem mais de 1 digito, usaria a funcao "stoi()"
            while(!digitos.empty() &&(digito > digitos.back()) && (apagados<D)){
                digitos.pop_back();
                apagados++; 
            }
            digitos.push_back(digito);
        }   
        
        // se no final das contas nao apaguei items o suficiente...
        while(apagados<D){
            // sei que vai ser menor ou igual ao elemento à esquerda dele
            digitos.pop_back(); 
            apagados++; 
        }
        for (auto& dig:digitos){
            cout << dig;
        }
        cout << '\n';
    }
    return 0;
}

