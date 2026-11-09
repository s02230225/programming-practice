#include <bits/stdc++.h>
using namespace std;
int main(){
    float c,xo,eps=100000,x;
    cin>>c;
    xo=sqrt(c);
    x=sqrt(c-xo);
    while(abs(x-xo)>eps){
        xo=x;
        x=sqrt(c-sqrt(xo));}
    cout<<x;
    return 0;}
