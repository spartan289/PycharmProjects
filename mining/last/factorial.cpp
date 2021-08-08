#include <bits/stdc++.h>

using namespace std;

//returns the factorial of n
int factorial(int n)
{
    if (n == 0)

        return 1;
    else

        return n * factorial(n - 1);
}

int main(){
    cout<<factorial(5);
}