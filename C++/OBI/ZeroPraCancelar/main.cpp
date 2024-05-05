#include <iostream>
#include <vector>
#include <numeric> // para usar o accumulate
using namespace std;

int main()
{
  int interacoes;
  int soma = 0;
  int valor = 0;
  vector<int> valores;
  cin >> interacoes;
  int val[interacoes];

  for (int i = 0; i < interacoes; i++)
  {
    cin >> valor;
    if (valor != 0)
    {
      valores.push_back(valor);
    }
    else
    {
      // preciso usar o valores.begin() pois essa funcao precisa de um iterador
      valores.pop_back(); // Usando o pop_back pois ele nao diminui o tamanho do meu vetor (poderia usar o erease() se quisesse)
    }
  }
  if (!valores.empty()){
      soma = accumulate(valores.begin(), valores.end(), 0); // valor inicial de 0
      cout << soma;
  }
  else{
    cout << 0;
  }

}

/*
se eu quisesse multiplicar um vetor:
int produto = std::accumulate(vetor.begin(), vetor.end(), 1, std::multiplies<int>());
*/
