#include <bits/stdc++.h>
using namespace std;

int main(){
    int a;
    cin>>a;
    map <string, int> M;
    vector <string> V;

    for (int i=0;i<a;i++){
        string b;
        cin>>b;
        if (b=="DEPOSIT"){
            string c;
            cin>>c;
            int d;
            cin>>d;
            if (M.find(c)!=M.end()) M[c]+=d;
            else{
                M[c]=d;
                V.push_back(c);}}
        if (b=="WITHDRAW"){
            string c;
            cin>>c;
            int d;
            cin>>d;
            if (M.find(c)!=M.end()) M[c]-=d;
            else {
                M[c]=-d;
                V.push_back(c);}}
        if (b=="BALANCE"){
            string c;
            cin>>c;
            if (M.find(c)!=M.end()) cout<<M[c]<<endl;
            else cout<<"ERROR"<<endl;}
        if (b=="TRANSFER"){
            string c1,c2;
            cin>>c1>>c2;
            int d;
            cin>>d;
            if (M.find(c1)==M.end()) M[c1]-=d;
            else {
                M[c1]=-d;
                V.push_back(c1);}
            if (M.find(c2)==M.end()) M[c2]+=d;
            else {
                M[c2]=+d;
                V.push_back(c2);}}
        if (b=="INCOME"){
            float d;
            cin>>d;
            for (auto el: V){
                M[el]+=M[el]*(d/100);}}
    }
    return 0;}
