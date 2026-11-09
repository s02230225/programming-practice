#include <iostream>
#include <vector>
using namespace std;
int main()
{
    int a,b;
    cin>>a>>b;
    vector<int> c(a);
    for (int i=0;i<a;i++) cin>>c[i];
    for (int i=0;i<b;i++){
        for (int j=i+1;j<a;j++){
            if (c[i]<c[j]){
                swap(c[i],c[j]);}}}
    cout<<c[b-1];
    return 0;
}
