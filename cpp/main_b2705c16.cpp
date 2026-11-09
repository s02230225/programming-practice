#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main(){
    multiset<ll> st; {
        int n;
        ll population;
        cin >> n;
        for(int i = 0; i < n; ++i){
            cin >> population;
            st.insert(population);}}
    ll result = 0;
    while(st.size() > 1){
        ll a = *st.begin();
        ll b = *(++st.begin());
        st.erase(st.begin());
        st.erase(st.begin());
        a += b;
        result += a;
        st.insert(a);}
    cout << result;
    return 0;}
