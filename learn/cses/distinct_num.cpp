#include <bits/stdc++.h>

using namespace std;
#define ll long long
int main()
{
    ll n = 5;
    ll arr[n];
    for (ll i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    map<int, int> m;
    for (ll i = 0; i < n; i++)
    {
        m[arr[i]]++;
    }
    ll count = 0;
    for (auto i : m)
    {
        count++;
    }
    cout << count;
}
