#include <bits/stdc++.h>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    
    int N, Q, x,caseCounter=0;
    while (cin >> N  >> Q && (N != 0 && Q != 0 )){
        caseCounter++;
        vector<int> marmores(N);
        for (auto& m:marmores){cin >> m;}
        sort(marmores.begin(), marmores.end());
        cout << "CASE# " << caseCounter << ":" << '\n';
        for (int i=0; i<Q; i++){
            cin >> x;
            auto it = lower_bound(marmores.begin(), marmores.end(), x);
            
            if (it == marmores.end() || *it != x){
                //estourou e saiu do vetor
                cout << x << " not found" << '\n';
            }else{
                cout << x << " found at " << (it-marmores.begin()) +1<< '\n';
            }
        }
    }

    return 0;
}

