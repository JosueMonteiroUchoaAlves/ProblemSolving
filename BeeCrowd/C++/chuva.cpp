#include <bits/stdc++.h>
// 3052 - Chuva (OBI 2019)
// https://judge.beecrowd.com/pt/problems/view/3052

using namespace std;

int main(){
    int l, c;
    cin >> l >> c;
    pair<int, int> inicio;

    vector<vector<char>> matriz(l, vector<char>(c));

    for (int i = 0; i<l; i++){
        for (int j = 0; j<c;j++){
           cin >>  matriz[i][j];
           if (matriz[i][j] == 'o'){
                inicio.first = i;
                inicio.second = j;
           }
        }
    }

    // Será um DFS
    stack<pair<int, int>> nextStep;
    nextStep.push(inicio);
    int i, j;
    while (!nextStep.empty()){
        i = nextStep.top().first;
        j = nextStep.top().second;
        nextStep.pop();
        // Coloco um 'o' na casa que estou agora
        matriz[i][j] = 'o';
        if (i < l-1){ // l-1 é a ultima linha, quando i == ultima linha nao quero que verifique mais nada
            if (matriz[i+1][j] == '#'){
                if (matriz[i][j-1] != 'o')
                {
                    nextStep.push({i, j-1});
                }
                if (matriz[i][j+1] != 'o'){
                    nextStep.push({i, j+1});
                }
            }else {
                nextStep.push({i+1, j});
            }
        }
    }

    for (int i = 0; i<l; i++){
        for (int j = 0; j<c;j++){
           cout << matriz[i][j];
        }
        cout << '\n'; // mais rapido que o endl
    }

    return 0;
}
