#include <iostream>

using namespace std;

int main()
{
    int voltas;
    cin >> voltas;
    switch (voltas % 8)
    {
    case 0:
        cout << 3;
        break;
    case 6:
        cout << 1;
        break;
    case 7:
        cout << 2;
        break;
    }
    return 0;
}
