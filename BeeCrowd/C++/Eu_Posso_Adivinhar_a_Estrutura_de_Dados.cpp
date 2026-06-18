#include <bits/stdc++.h>

using namespace std;

int main(){
    int N, op, x;

    while (cin >> N){
        stack<int> pilha;
        queue<int> fila;
        priority_queue<int> filaPrioritaria;
        int p=1, f=1, fp=1;
        for (int i=0; i<N; i++){
            cin >> op >> x;
            if (op == 1){
                pilha.push(x);
                fila.push(x);
                filaPrioritaria.push(x);
            }else{
                if(fila.front() != x || f==0){
                    f=0;
                }else{
                    fila.pop();
                }
                if(pilha.top() != x || p==0){
                    p=0;
                }else{
                    pilha.pop();
                }
                if(filaPrioritaria.top() != x || fp==0){
                    fp=0;
                }else{
                    filaPrioritaria.pop();
                }
            }
        }
        if (p + f + fp > 0){
            if (p + f + fp > 1){
                    cout << "not sure" << '\n';
                }
                else{
                    if (p){
                        cout << "stack" << '\n' ;
                    }
                    if (f){
                        cout << "queue" << '\n' ;
                    }
                    if (fp){
                        cout << "priority queue" << '\n' ;
                    }
                }
                
            }else{
                cout << "impossible" << '\n';
            }    
    }

    return 0;
}

