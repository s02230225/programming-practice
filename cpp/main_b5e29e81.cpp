#include <iostream>
using namespace std;

int main()
{
    int a;
    cin>>a;
    if (a%100/10==1 or a%10==7 or a%10==8 or a%10==9 or a%10==0) cout<<a<<" bochek";
    else{if(a%10==2 or a%10==3 or a%10==4) cout<<a<<" bochi";
    else cout<<a<<" bocha";}
    return 0;
}
