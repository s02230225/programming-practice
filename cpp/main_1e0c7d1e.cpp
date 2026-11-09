#include <bits/stdc++.h>
using namespace std;
int main(){
    string str, letters;
    getline(cin, str);
    vector <int> meets(26);
    for (int i = 0; i < str.size(); i++){
        if (isalpha(str[i])) {
            str[i] = toupper(str[i]);
            meets[(int)str[i] - 65] += 1;}}
    int max = *max_element(meets.begin(), meets.end());
    for (int i = 0; i < meets.size(); ++i) {
        if (meets[i] == max) letters.push_back((char)i + 65);}
    cout << letters << endl << max;
    return 0;}
