#include <iostream>
#include <string>
using namespace std;

int main()
{
    string a;
    getline(cin, a);
    int b=a.length();
    for (int i=0;i<b-1;i++){
        cout<<a[i]<<"*";}
    cout<<a[b-1];
    return 0;
}
