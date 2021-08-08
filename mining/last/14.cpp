/*Write a program to accept an input n from the user and graphically represent 
the values of T(n) where n varies from 0 to n for the recurrence relations. 
For e.g. T(n) = T(n-1) + n, T(0) = 1, T(n) = T(n-1) + n^2, T(0) =1, T(n) = 2*T(n)/2 + n, T(1)=1.*/

#include<iostream>
using namespace std;

int eq1(int n)  //for equation1 
{
	if(n==0)  
	{
		return 1; //base case
	}
	else
	{
		return eq1(n-1)+n;
	}
}
int eq2(int n) //equation 2
{
	if(n==0)
	{
		return 1;  //base case 
	}
	else
	{
		return eq2(n-1)+n*n;
	}
}
int eq3(int n) //equation 3
{
	if(n==1)
	{
		return 1; //base case 
	}
	else
	{
		return (2*eq3(n/2))+n;
	}
}

int table(int n,int c) //table 
{
	int out;
	int ans[n+1];
	ans[0]=1;
	for(int i=1;i<=n;i++)
	{
		if(c==1)
		ans[i]=eq1(i);
		else if(c==2)
		ans[i]=eq2(i);
		else if(c==3)
		ans[i]=eq3(i);
	}
	cout<<"-----------";
	cout<<endl;
	for(int i=n;i>=0;i--)
	{
		cout<<"T("<<i<<")   | "<<ans[i];
		cout<<endl;
	}

		cout<<"-----------";
	
}



int main(){
	int n,i;
	int choice;
	do
	{
		cout<<"ENTER 1 to solve T(n) = T(n-1) + n, T(0) = 1"<<endl;
		cout<<"ENTER 2 to solve T(n) = T(n-1) + n^2, T(0) =1"<<endl;
		cout<<"ENTER 3 to solve T(n) = 2*T(n/2) + n, T(1) =1"<<endl;
		cout<<endl;
		cin>>choice;
		if(choice>=4)
		{
			cout<<"WRONG CHOICE !"<<endl;
			cout<<"Exiting"<<endl;
			exit(0);
		}
		cout<<"\nEnter the value of n : ";
		cin>>n;
		if(choice==1)
		{
			cout<<"\nT(n) = T(n-1) + n for n="<<n<<" is : "<<eq1(n);
			cout<<"\n\nTable is : "<<endl;
			table(n,choice);
		}
		else if(choice==2)
		{
			cout<<"\nT(n) = T(n-1) + n^2 for n="<<n<<" is : "<<eq2(n);
			cout<<"\n\nTable is : "<<endl;
			table(n,choice);
		}
		else if(choice==3)
		{
			cout<<"\nT(n) = 2*T(n/2) + n for n="<<n<<" is : "<<eq3(n);
			cout<<"\n\nTable is : "<<endl;
			table(n,choice);
		}
		
		cout<<"\nPress 1 to continue: ";
		cin>>i;
	}while(i==1);
}