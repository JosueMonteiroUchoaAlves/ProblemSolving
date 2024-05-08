#include <iostream>
#include <bits/stdc++.h>
using namespace std;

// https://olimpiada.ic.unicamp.br/pratique/p1/2011/f1/pas/
// or
// https://neps.academy/br/exercise/528
// Usando Two Pointers
// PASSED ALL THE TESTS
/*
    1 - indicar onde eu estou no meu vetor
    2 - indicar o indice inicial de um "novo vetor artificial"
        que e quem eu vou levar em conta na hora de comparar
*/
int total_possibilidades = 0;
int valor;
int nV = 0;
int tam_vetor = 0;
vector<int> vetor;

int main()
{

  cin >> tam_vetor;

  // Mesmo dessa forma (com o uso de loops) o C++ pega valores na mesma linha
  for (int i = 0; i < tam_vetor; i++)
  {
    cin >> valor;
    vetor.push_back(valor);
  }

  for (int i = 1; i < tam_vetor; i++)
  {
    if (vetor[i] - vetor[i - 1] !=  vetor[nV + 1] - vetor[nV])
    {
      total_possibilidades += 1;
      nV = i;
      i++;
    }
  }
  total_possibilidades++;
  cout << total_possibilidades;
  // +1 pois eu estava usando ele como indice entao ele valia 1 a menos
  return 0;
}
