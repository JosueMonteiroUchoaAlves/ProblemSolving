#include <iostream>
#include <bits/stdc++.h>
using namespace std;

//https://neps.academy/br/exercise/1735

const int MAX = 80;

int main()
{
  int N;
  int counter = 0;
  string bloco[MAX];
  string variable;
  string resp = "";

  cin >> N;

  for (int i=0 ; i<N; i++){
    cin >> variable;
    for (int j=1 ; j<variable.size(); j++){
      if(variable[j] == variable[j-1]){
        counter ++;
      }
      else{
        counter++;
        resp = resp + " " + to_string(counter) + " " + variable[j-1];
        counter = 0;
      }

    }
    counter++;

    resp = resp + " " + to_string(counter) + " "+ variable[variable.size()-1] + "\n";
    counter = 0;
  }
  cout<<resp;
}
