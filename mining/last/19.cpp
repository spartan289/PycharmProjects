/*Given an adjacency matrix of a graph, write a program to check whether a given set of vertices {v1,v2,v3.....,vk} 
forms an Euler path / Euler Circuit (for circuit assume vk=v1).*/

#include<iostream>

using namespace std;

class Euler
{
	private: 
	int** a;
	int v,even,odd;
	char ch[20];
	public:
		Euler()
		{
			v=0;
			a=NULL;
			even=odd=0;
		}
		Euler(int m,char c[])
		{
			v=m;
			a= new int*[m];
			for(int i=0;i<v;i++)
			{
				a[i]=new int[v];
			}
			for(int i=0;i<v;i++)
			{
				for(int j=0;j<v;j++)
				{
					a[i][j]=0;
				}
			}
			for(int i=0;i<v;i++)
			{
				ch[i]=c[i];
			}
		}

		void Undirected(char ch1,char ch2)
		{
			for(int i=0;i<v;i++)
			{
				if(ch1==ch[i])
				{
					for(int j=0;j<v;j++)
					{
			   			if(ch2==ch[j])
						{
							a[i][j]++;
							a[j][i]++;
						}
					}
				}
			}
		}
		void Directed(char ch1,char ch2)
		{
			for(int i=0;i<v;i++)
			{
				if(ch1==ch[i])
				{
				for(int j=0;j<v;j++)
					{
			   			if(ch2==ch[j])
						{
							a[i][j]++;
						}
					}
				}
			}
		}
		void show()
		{
			cout<<"  ";
			for(int i=0;i<v;i++)
			{
				cout<<ch[i]<<"  ";
			}
			cout<<endl;
			for(int i=0;i<v;i++)
			{
				cout<<ch[i]<<"  ";
				for(int j=0;j<v;j++)
				{	
					cout<<a[i][j]<<"  ";
				}cout<<endl;
			}
		}
		int eulerCircuit()
		{
			even=0;
			int s=0;
			for(int i=0;i<v;i++)
			{
				for(int j=0;j<v;j++)
				{
					s+=a[i][j];
				}
				if(s%2==0)
				{
					even++;
				}
				else
				odd++;
				s=0;
			}
			if(even==v)
			return 1;
			else
			return 0;
		}
		int eulerPath()
		{
			int flag=0;
			int check=eulerCircuit();
			if(check==1)
				flag=1;
			else
			{
				if(odd==0)
				flag=1;
				else
				flag=0;
			}
			return flag;
		}
		int eulerCircuitD()
		{
			int s1,s2;
			for(int i=0;i<v;i++)
			{
				for(int j=0;j<v;j++)
				{
					s1+=a[i][j];
					s2+=a[j][i];
				}
			if((s1-s2)!=0)
			return 0;
			if((s2-s1)!=0)
			return 0;
			s1=s2=0;
		}
		return 1;
		}
		int eulerPathD()
		{
			int c1,c2=0;
			int s1,s2=0;
			for(int i=0;i<v;i++)
			{
				for(int j=0;j<v;j++)
				{
					s1+=a[i][j];
					s2+=a[j][i];
				}
			if((s1-s2)==1)
			c1++;
			else
			c2++;
			s1=s2=0;
		}
		if(c1!=1&&c2!=1)
		return 0;
		else return 1;
		}
};
int main()
{
	int f;
	int** a;
	cout<<"\nEnter the number of vertices: ";
	int v;
	cin>>v;
	char ch[v];
	cout<<"\nEnter the vertices: ";
	for(int i=0;i<v;i++)
	{
		cin>>ch[i];
	}
	Euler ob(v,ch);
	
	
	cout<<"\nEnter the number of edges: ";
	int e;
	cin>>e;
	char ch1,ch2;
	cout<<"\nEnter 1 to check for undirected ";
	cout<<"\nEnter 2 to check for directed : ";
	int choice;
	cin>>choice;
	for(int i=0;i<e;i++)
	{
		cout<<"\nEnter vertex 1 for edge "<<i+1<<" : ";
		cin>>ch1;
		cout<<"\nEnter vertex 2 for edge "<<i+1<<" : ";
		cin>>ch2;
		if(choice==1)
		ob.Undirected(ch1,ch2);
		else
		ob.Directed(ch1,ch2);
	}
	cout<<"\n";
	ob.show();
	do{
	cout<<"\n\n";
	cout<<"\nEnter 1 to check euler path : ";
	cout<<"\nEnter 2 to check euler circuit : ";
	int c;
	cin>>c;
	if(choice==1)
	{
		if(c==1)
		{
		int flag=ob.eulerPath();
		if(flag==1)
		cout<<"\nIt is a Euler Path !!";
		else
		cout<<"\nIt is not a Euler Path !!";
		}
		else
		{
			int flag=ob.eulerCircuit();
			if(flag==1)
			cout<<"\nIt is a Euler Circuit !!";
			else
			cout<<"\nIt is not a Euler Circuit !!";
		}
	}
	else if(choice ==2)
	{
		if(c==1)
		{
		int flag=ob.eulerPathD();
		if(flag==1)
		cout<<"\nIt is a Euler Path !!";
		else
		cout<<"\nIt is not a Euler Path !!";
		}
		else
		{
			int flag=ob.eulerCircuitD();
			if(flag==0)
			cout<<"\nIt is a Euler Circuit !!";
			else
			cout<<"\nIt is not a Euler Circuit !!";
		}
	}
	cout<<"\n\nEnter 1 to continue:";
	cin>>f;
}while(f==1);
}