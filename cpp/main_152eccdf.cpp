#include <bits/stdc++.h>
using namespace std;
int main(){
    bool r=true;
    long long w=0;
    vector <long long> q(w);
    while (r){
        string a;
        cin>>a;
        if (a=="push"){
            long long b;
            cin>>b;
            q.push_back(b);
            w++;
            cout<<"ok"<<endl;}
        else{if (a=="pop" and w==0){
            cout<<"error"<<endl;}
        else{if (a=="pop" and w>0){
            cout<<q.back()<<endl;
            q.pop_back();
            w=w-1;}
        else{if (a=="back" and w==0){
            cout<<"error"<<endl;}
        else{if (a=="back" and w>0){
            cout<<q.back()<<endl;}
        else{if (a=="size"){
            cout<<w<<endl;}
        else{if (a=="clear"){
            while (w>0){
                q.pop_back();
                w=w-1;}
            cout<<"ok"<<endl;}
        else{if (a=="exit"){
            r=false;
            cout<<"bye"<<endl;}}}}}}}}}
    return 0;}
