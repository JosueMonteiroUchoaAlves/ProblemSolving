#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
  vector<int> idades = {0, 0, 0};
  for (int i = 0; i < 3; i++)
  {
    cin >> idades[i];
  }
  sort(idades.begin(), idades.end()); // Vai organizar a lista do comeco ao fim
  cout << idades[1];
  return 0;
}
