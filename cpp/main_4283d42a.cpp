#include <bits/stdc++.h>
using namespace std;
bool ok(int x, int m, vector <int> h){
    int s=0;
    for (auto i: h){
        if (i%x==0) s+=i/x;
        else s+=i/x+1;}
    if (s<=m) return true;
    else return false;}
int main(){
    int n,m,l=0,r=0;
    cin>>n;
    vector <int> h(n);
    for (int i=0;i<n;i++){
        int q;
        cin>>q;
        h[i]=q;
        if (r<q) r=q;}
    cin>>m;
    while (r-l>1){
        int x=(r+l)/2;
        if (ok(x,m,h)) r=x;
        else l=x;}
    if (m<n) cout<<-1;
    else cout<<r;
    return 0;}
