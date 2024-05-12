#include <iostream>
#include <bits/stdc++.h>
using namespace std;

// https://neps.academy/br/exercise/173x5

const int MAX = 80;

int main()
{
  int N;
  int counter = 0;
  string bloco[MAX];
  string variable;
  string variable2;
  vector<string> resp = {};

  cout << "deu";

  cin >> N;

  for (int i = 0; i < N; i++)
  {
    cin >> variable;

    for (size_t j = 1; j < variable.size(); j++) // Usando o size_t pra não dar warning por causa da comparacao com size
    {
      cout << (variable[j] == variable[j - 1]) ? true : false;
      if (variable[j] == variable[j - 1])
      {
        counter++;

        resp.push_back({}); // adiciona um vetor
        variable2 = ((resp[i].size() > 0) ? " " : "") + to_string(counter) + " " + variable[j - 1];
        resp[i].append(variable2);
      }
      else
      {
        counter++;
        variable2 = ((resp[i].size() > 0) ? " " : "") + to_string(counter) + " " + variable[j - 1];
        resp[i].append(variable2); // concatenacao de strings
        counter = 0;
      }
    }
    counter++;
    variable2 = " " + to_string(counter) + " " + variable[variable.size() - 1] + "\n";
    resp[i].append(variable2);
    counter = 0;
  }
  for (string i : resp)
  {
    cout << i << "\n";
  }
}
