#include <iostream>

using namespace std;

int main()
{
  int A;
  int B;

  cin >> A >> B;
  if (B < A){
    swap(B, A);
  }

  cout << A-(B-A);
    return 0;
}
