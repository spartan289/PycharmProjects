#include <bits/stdc++.h>

using namespace std;
void permute_string(string s, int l, int r, set<string> &res)
{
    if (l == r)
    {
        res.insert(s);
        return;
    }
    for (int i = l; i <= r; i++)
    {
        swap(s[l], s[i]);
        permute_string(s, l + 1, r, res);
        swap(s[l], s[i]);
    }
}
int main()
{
    string s;
    cin >> s;
    int n = s.length();
    set<string> res;
    permute_string(s, 0, n - 1, res);
    cout << res.size() << endl;
    for (auto i : res)
    {
        cout << i << endl;
    }
    return 0;
}