#include <iostream>
#include <bits/stdc++.h>
using namespace std;
// Divisao do Tesouro
// https://olimpiada.ic.unicamp.br/pratique/pj/2020/f1/tesouro/
// or
// https://neps.academy/br/exercise/976

// Declarando do lado de fora para as variaveis virem zeradas
int tesouro;
int marinheiros;

int main()
{
  cin >> tesouro;
  cin >> marinheiros;
  /* capitao vale 2 marinheiros
     (marinheiros + capitao) = quantidade que cada um recebe
     entao multiplico por 2 pra saber quanto o capitao ficou
  */
  cout << (tesouro / (marinheiros + 2)) * 2 << endl;
  return 0;
}
