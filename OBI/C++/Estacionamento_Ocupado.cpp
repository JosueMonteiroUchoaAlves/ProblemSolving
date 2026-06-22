#include <iostream>
#include <bits/stdc++.h>

using namespace std;

// https://neps.academy/br/exercise/2025
// PASSED ALL THE TESTS
const int MAX = 100;
int ocupados[MAX];

int main()
{
  int N = 0;
  char caracter = ' ';
  int total = 0;

  cin >> N;
  for (int i = 0; i < N; i++)
  {
    cin >> caracter;
    if (caracter == 'C')
    {
      ocupados[i] = 1;
    }
  }
  for (int i = 0; i < N; i++)
  {
    cin >> caracter;
    if (caracter == 'C' && ocupados[i] == 1)
    {
      total += 1;
    }
  }
  cout << total;
  return 0;
}
