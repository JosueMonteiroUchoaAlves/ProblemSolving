#include <iostream>
#include <bits/stdc++.h>
using namespace std;

// https://neps.academy/br/exercise/1735

const int MAX = 80;

int main()
{
  int N;
  int counter = 0;
  string bloco[MAX];
  string variable;
  string variable2;
  vector<string> resp = {};

  cin >> N;

  for (int i = 0; i < N; i++)
  {
    cin >> variable;

    for (size_t j = 1; j <= variable.size(); j++) // Usando o size_t pra não dar warning por causa da comparacao com size
    {
      if (variable[j] != variable[j - 1])
      {
        counter = 1;

        resp.push_back({}); // adiciona um vetor
        variable2 = ((resp[i].size() > 0) ? " " : "") + to_string(counter) + " " + variable[j - 1];
        resp[i].append(variable2);
      }
      else
      {
        if (resp.size() == 0)
        {
          resp.push_back({}); // adiciona um vetor
        }
        counter++;
        variable2 = ((resp[i].size() > 0) ? " " : "") + to_string(counter) + " " + variable[j - 1];
        resp[i].append(variable2); // concatenacao de strings
        counter = 0;
      }
    }
  }
  for (string i : resp)
  {
    cout << i;
  }
}
