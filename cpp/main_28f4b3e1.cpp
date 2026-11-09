#include <iostream>
using namespace std;

int main(){
    int a,b=1,c=0;
    cin>>a;
    for (int i=1;i<=a;i++){
        b=b*i;
        c+=b;}
    cout<<c;
    return 0;
}
