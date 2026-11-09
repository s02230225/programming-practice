#include <iostream>
using namespace std;

int main()
{
    string a;
    cin>>a;
    for (int i=0;i<a.size();i+=2){
        cout<<a[i]<<"";}
    for (int j=1;j<a.size();j+=2){
        cout<<a[j]<<"";}
    return 0;
}
