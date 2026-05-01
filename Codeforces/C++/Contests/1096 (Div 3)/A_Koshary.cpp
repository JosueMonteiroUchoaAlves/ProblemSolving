#include <bits/stdc++.h>

using namespace std;

int main(){
    int n;
    cin >> n;
    int x, y;

    for (int i =0; i<n; i++)
    {
        cin >> x >> y;
        if ((x % 2 == 1) && (y % 2 == 1))
        {
            cout << "NO" << '\n';
        }
        else{
            cout << "YES" << '\n';
        }
    }

    return 0;
}
