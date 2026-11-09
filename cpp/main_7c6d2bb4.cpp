#include <bits/stdc++.h>
using namespace std;

vector<int> merge(vector<int> a, vector<int> b) {
    vector<int> res;
    int i = 0;
    int j = 0;
    while (i < a.size() && j < b.size()) {
        if (a[i] <= b[j])
            res.push_back(a[i++]);
        else
           res.push_back(b[j++]);
    }
    while (i < a.size())
        res.push_back(a[i++]);
    while (j < b.size())
        res.push_back(b[j++]);
    return res;}

vector<int> msort(vector<int> a) {
    if (a.size() <= 1)
        return a;
    int k = a.size() / 2;
    return merge(
        msort(vector<int>(a.begin(), a.begin() + k)),
        msort(vector<int>(a.begin() + k, a.end())));}

int main(){
    int aa;
    cin>>aa;
    vector <int> a(aa);
    for (int i=0;i<aa;i++){
        cin>>a[i];}
    vector <int> c(aa);
    for (int i=0;i<aa;i++){
        c[i]=a[i];}
    c=msort(c);
    for (int i=0;i<aa;i++){
        cout<<c[i]<<" ";}
    return 0;}
