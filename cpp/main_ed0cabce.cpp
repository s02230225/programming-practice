#include <iostream>
using namespace std;
int main(){
    int a,b,c,d;
    if (a>b){
        a=d;
        a=b;
        b=d;
    }
    if (a>c){
        a=d;
        a=c;
        c=d;
    }
    if (b>c){
        b=d;
        b=c;
        c=d;
    }
    cout<<a<<" "<<b<<" "<<c<<endl;
    return 0;
}

