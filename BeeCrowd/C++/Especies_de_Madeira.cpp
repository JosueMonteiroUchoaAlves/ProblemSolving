#include <bits/stdc++.h>

using namespace std;

int main(){
    int N;
    string especie;
    // char buffEater;
    cin >> N;
    cin.ignore();
    cin.ignore();
    //cin.get(buffEater);
    //cin.get(buffEater);
    for(int i=0;i<N;i++){ 
        map<string, double> percentuais;
        int total=0;
        while (getline(cin, especie) && especie!=""){
            percentuais[especie]++;
            total++;
        }
        if (i!=0){
            cout << '\n';
        }
        for (auto& item: percentuais){
            cout << fixed << setprecision(4) << item.first << " " << (item.second/total)*100 << '\n';
        }     
        
    }
    
    return 0;
}

