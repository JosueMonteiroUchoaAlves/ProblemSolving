#include <iostream>
using namespace std;

// DAY 1 LEARNING C++
// CODE FULLY WORKING AND 100% PROUDLY MADE BY MYSELF

int main(){
  string consoantes = "bcdfghjklmnpqrstvxz";
  string vogalProx  = "aaeeeiiiiooooouuuuu";
  string proxConsoante = "cdfghjklmnpqrstvxzz";
  string palavra = "";
  string cifra;
  cin >> cifra;
  int i = 0;
  for (i;i< cifra.size(); i++){
    int indiceCons = consoantes.find(cifra[i]);//NoPosition
    if (indiceCons != string::npos){ // Se foi achado...
      palavra = palavra + cifra[i] + vogalProx[indiceCons] + proxConsoante[indiceCons];
    }
    else{
      palavra+=cifra[i]; // Concatenacao de strings
    }
  }
  cout  << palavra;

  return 0;
}
/*
npos e uma constante estatica definida na classe std::string em C++.
Ela e usada para representar um valor invalido ou uma posicao nao encontrada em uma string.
Geralmente, npos e definido como o maior valor possivel para o tipo size_t,
que e o tipo de dado usado para representar tamanhos de conteineres em C++.
Isso significa que npos geralmente e igual a std::string::npos, que e equivalente
a static_cast<size_t>(-1).
Quando voce usa metodos como find() em uma string e o caractere ou substring nao
e encontrado, o metodo retorna std::string::npos para indicar que a busca nao teve exito.
*/
// O operador :: acessa membros de namespaces
