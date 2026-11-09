#include <iostream>

using namespace std;

int main()
{
    int b=0;
    for (int a=100000;a<1000000;a+=1){
    if (a<100000 or a>999999) cout<<"";
    else{
        if (a%39!=0 or a%71!=0) cout<<"";
        else{
            if (a/100000+(a/1000)%10+(a/10)%10!=21 or (a/10000)%10+(a/100)%10+a%10!=21) cout<<"";
            else{
                    cout<<"yes"<<" "<<a<<endl;
                    b=a;
            }
        }
    }}
    cout<<b<<endl;
    return 0;
}
