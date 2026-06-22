#include <iostream>
#include <bits/stdc++.h>
// Colheita

// https://neps.academy/br/exercise/2698

using namespace std;

const int MAX_SIZE = 1000;

// Os parenteses chamam o construtor do vetor, com: tamanho e elemento
int main()
{
  int l;
  int c;
  int maior = -99999;
  vector<int> cordMaior = {-1, -1};
  vector<vector<int>> matrix(MAX_SIZE, vector<int>(MAX_SIZE, 0));
  vector<vector<int>> differences;

  cin >> l >> c;

  for (int i = 0; i < l; i++)
  {
    for (int j = 0; j < c; j++)
    {
      cin >> matrix[i][j];
    }
  }
  differences = matrix;

  for (int i = 0; i < l; i++)
  {
    for (int j = 0; j < c; j++)
    {
      if (i == 0 && j == 0)
      {
        continue;
      }
      if (maior < matrix[i][j])
      {
        maior = matrix[i][j];
        cordMaior[0] = i;
        cordMaior[1] = j;
      }
      if (i > 0)
      {
        differences[i][j] = min(differences[i][j], differences[i - 1][j]);
      }
      if (j > 0)
      {
        differences[i][j] = min(differences[i][j], differences[i][j - 1]);
      }
    }
  }

  cout << (maior - differences[cordMaior[0]][cordMaior[1]]);
  return 0;
}
