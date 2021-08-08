//6.	Write a Program to implement Tower of Hanoi using recursion.
#include<iostream> 
using namespace std; 
  
void towerofhanoi(int n, char from, char to, char temp) 
{ 
    if(n==1) 
    { 
        cout<<"Move disk 1 from "<<from<<" to "<<to<<endl; 
        return; 
    } 
    towerofhanoi(n-1, from, temp, to); 
    cout<<"Move disk "<<n<<" from "<<from<<" to "<<to<<endl; 
    towerofhanoi(n-1, temp, to, from); 
} 
  
int main() 
{ 
    cout<<"enter no of rings ";
    int n;
    cin>>n;
    towerofhanoi(n,'A','C','B'); 
    return 0; 
}