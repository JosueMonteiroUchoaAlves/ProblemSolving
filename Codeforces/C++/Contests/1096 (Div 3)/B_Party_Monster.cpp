#include <bits/stdc++.h>

using namespace std;

int main(){
    int n, sum=0, seqSize;
    cin >> n;
    string sequence;

    for (int i =0; i<n; i++)
    {
        cin >> seqSize;
        cin >> sequence;
        for (char c : sequence)
        {
            if (c == '(')
            {
                sum++;
            }
            else
            {
                sum--;
            }
        }
        if (sum == 0)
        {
            cout << "YES" << '\n';
        }
        else
        {
            cout << "NO" << '\n';
        }
        sum = 0;
    }

    return 0;
}
