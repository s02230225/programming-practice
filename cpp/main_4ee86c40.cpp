#include <iostream>
#include <cmath>
using namespace std;
int nod(int a, int b){
    if (b>0) return nod(b, a%b);
    else return a;
}
int main()
{
    int x1,y1,x2,y2,a,b,d;
    cin>>x1>>y1>>x2>>y2;
    a=abs(x1-x2);
    b=abs(y1-y2);
    d=nod(a,b);
    cout<<d*(a/d+b/d-1);
    return 0;
}
