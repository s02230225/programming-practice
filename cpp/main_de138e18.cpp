#include <bits/stdc++.h>
using namespace std;
vector<int> f(int n){
    vector<int> p;
    for (int d = 2; d * d <= n; ++d) {
        while (n % d == 0){
            p.push_back(d);
            n /= d;
        }
    }
    if (n > 1)
        p.push_back(n);
    return p;}

int main(){
    int n,a,b,c;
    cin>>n;
    vector<int> p;
    p=f(n);
    a=p[0];
    b=1;
    c=p.size();
    for (int i=1;i<=c;i++){
        if (p[i]==a and i!=c){
            b+=1;}
        else{
            if (b==1) cout<<a;
            else cout<<a<<"^"<<b;
            if (i!=c) cout<<"*";
        a=p[i];
        b=1;}}
    return 0;}
