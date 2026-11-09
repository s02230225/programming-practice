#include <bits/stdc++.h>
using namespace std;
int main(){
    int n,m,cnt;
    string s;
    cin>>n>>m;
    map<string,int> dict;
    vector <int> ans(n,0);
    for(int i=0;i<m;i++){
        cin>>cnt>>s;
        dict[s]=cnt;}
    for (auto& item: dict){
        ans[item.second-1]++;}
    for(int i=0;i<n;i++){
        cout<<ans[i]<<' ';}
    return 0;}
