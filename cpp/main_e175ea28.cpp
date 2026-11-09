#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int gcd(int a, int b){
    int tmp;
    while(b != 0){
        tmp=a%b;
        a=b;
        b=tmp;}
    return a;}
int main(){
    vector<int> factors;
    int n,k,sz,a,b,c;
    cin >> n;
    k=1;
    while (k*k<=n){
        if (n%k==0){
            factors.push_back(k);
            if (n/k != k) factors.push_back(n/k);}
        k++;}
    sort(begin(factors), std::end(factors));
    sz=factors.size();
    c=0;
    for (int i=0; i<sz-1; i++)
        for (int j=i+1; j<sz; j++){
            a=factors[i];
            b=factors[j];
            if ((gcd(a,b)==1) && (a*b<=n)){
                c++;}}
    cout << c;
    return 0;}
