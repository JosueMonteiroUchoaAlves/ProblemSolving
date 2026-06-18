#include <bits/stdc++.h>

using namespace std;

int main(){
    int N, Q, x,caseCounter=0;
    while (cin >> N  >> Q && (N != 0 && Q != 0 )){
        caseCounter++;
        vector<int> marmores(N);
        // inverto todos os numeros para negativo
        // dessa forma o primeiro que eu achar sendo maior que x na verdade sera
        // o primeiro menor que ele, dessa forma estando exatamente ao lado dele.
        for (auto& m:marmores){cin >> m; (m=-m);}
        sort(marmores.begin(), marmores.end());
        cout << "CASE# " << caseCounter << ":" << '\n';
        for (int i=0; i<Q; i++){
            cin >> x;
            x = -x;
            if (binary_search(marmores.begin(), marmores.end(), x)){
                // retiro o valor achado de N pois esta organizado ao contrario
                // somo +1 pois meu numero é logo apos esse que é o primeiro menor
                cout << -x << " found at " << (N-(upper_bound(marmores.begin(), marmores.end(), x) - marmores.begin()))+1 << '\n';
            }else{
                cout << -x << " not found" << '\n';
            }
        }
    }

    return 0;
}

