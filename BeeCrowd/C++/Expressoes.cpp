#include <bits/stdc++.h>

using namespace std;

int main(){
    int N;
    char c;
    map<char, char> oposto = {
        {')','('},
        {']','['},
        {'}','{'},
    };
    stack<char> pilha;
    bool invalid=false;
    cin >> N;
    cin.ignore();

    for (int i=0; i<N; i++){
        while (cin.get(c) && c != '\n'){
            if (c == '{' || c == '[' || c == '(' ){
                pilha.push(c);
                continue;
            }
            if(pilha.empty() || oposto[c] != pilha.top()){
                invalid=true;
            }
            else {
                pilha.pop();
            } 
        }
        if(invalid ==true || !pilha.empty()){
            cout << "N" << '\n';
        }else{
            cout << "S" << '\n';
        }
        stack<char>().swap(pilha);
        invalid=false;
    }

    return 0;
}

