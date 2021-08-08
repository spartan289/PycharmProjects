#include <bits/stdc++.h>
using namespace std;

int main(){
    int degree;
    cout<<"Enter the degree of your polynomial: ";
    cin >> degree;
    int poly[degree+1];
    cout<<endl;
    cout<<endl;

    for(int i=0;i<=degree;i++){
        cout <<"Enter the coefficient of x raised to power "<<degree-i<<" ";
        int coefficient;
        cin >> coefficient;
        poly[i]=coefficient;
    }
    cout<<endl;
    cout<<endl;

    cout<<"your polynomial is f(x)= ";
    for(int i=0;i<=degree;i++){
        cout<<poly[i]<<"x^"<<degree-i;
        if(i!=degree){
            cout<<" + ";
        }
    }
    cout<<endl;
    cout<<endl;

    
    cout<<"Enter the value of x for which you want to compute the value of x ";
    int x;
    cin >> x;
    int sum=0;
    for(int i=0;i<=degree;i++){
        sum+=poly[i]*(pow(x,(degree-i)));
    }
    cout<<"Value is : "<<sum; 
} 