#include<iostream>
#include<iomanip>

using namespace std;

class GRAPH
{
    private:
            int** arr;
            int  **b;
            char* arr1;
            int size;

    public:
           GRAPH();  // default constructor
            GRAPH(int s);
           void input();         //function for set the size of array
           void enter(int num);         // input funtion
          void multiplication(int n);
         void output();
         void path_len(char a, char b,int n);
}; 
//class declaration

// method defination

GRAPH:: GRAPH()
     {
         int** arr=0;
         int** b =0;
         char* arr1=0;
         int size=0;

     }//default constructur
     
GRAPH::GRAPH(int s)

{
	size =s;
	  arr1= new char [size];
	  
	    arr=new int*[size];
       
         for(int i=0;i<size;i++)
         {
             arr[i]=new int [size];
         }

         for(int i=0;i<size;i++)
         {
             for(int j=0;j<size;j++)
             {
             arr[i][j]=0;
             }
         }
         
         
	  b=new int*[size];
       
         for(int i=0;i<size;i++)
         {
             b[i]=new int [size];
         }

         for(int i=0;i<size;i++)
         {
             for(int j=0;j<size;j++)
             {
                 b[i][j]=0;
             }
         }
}


     void GRAPH:: input()
     {
          

       
         cout<<"enter the vertices "<<endl;
         
         for(int i=0;i<size;i++)
         {cout<<"-->";
             cin>>arr1[i];
         }
         
         cout<<"\n\tthe vertices u enter is "<<endl;
         cout<<"\t{";
         for(int i=0;i<size;i++)
         {
             cout<<arr1[i];
             if (i!=size-1)
             {cout<<",";}
         }
         cout<<"}"<<endl;
       
       


     }// size setting funtion
     void GRAPH::enter(int num)
     {
         char x,y;
         char pos_x;
         int pos_y;
         
         for(int k=0;k<num;k++)
         {   
             cout<<endl;
             cout <<"enter the pair of adjacent vertices"<<k+1<<endl;
             cin>>x>>y;
          
          for(int i=0;i<size;i++)
             {
                 if( arr1[i]==x)
                 pos_x=i;

                 if( arr1[i]==y)
                 pos_y=i;
             }

             for(int l=0;l<size;l++)
             {
                 for(int m=0;m<size;m++)
                 {
                     if((pos_x==l)&&(pos_y==m)||(pos_x==m)&&(pos_y==l))
                     arr[l][m]+=1;
                 }
             }
             
         }

         cout<<"\nthe Adjacency matrix is \n"<<endl;
         cout<<"   ";
           for(int l=0;l<size;l++)
           {
           	cout<<setw(3)<<arr1[l];
           	
           }
           cout<<endl;
         
         for(int l=0;l<size;l++)
             {  
             cout<<arr1[l]<<" ";
                 for(int m=0;m<size;m++)
                 {
                     cout<<setw(3)<<arr[l][m];
                 }
                 cout<<endl;
             }
     }                    //input taking funtion
     

void GRAPH:: multiplication(int n){
	  int**c;
      c=new int*[size];
       
         for(int i=0;i<size;i++)
         { 
             c[i]=new int [size]; 
         }

         for(int i=0;i<size;i++)
         {   for(int j=0;j<size;j++)
             { c[i][j]=0;} 
          }
         
 for(int i=0;i<size;i++)
         { for(int j=0;j<size;j++)
             {  c[i][j]=arr[i][j];  }
         }
         
         
	for(int m = 0;m<n-1;m++)
	{
    	for(int i=0; i<size;i++)
      {  for(int j=0;j<size;j++)
		 {	for(int k=0;k<size;k++)
			{ b[i][j]+=arr[i][k]*c[k][j];}
		}
 	}
   	for(int i=0;i<size;i++)
         { for(int j=0;j<size;j++)
             {  arr[i][j]=b[i][j]; }
         }
           for(int i=0;i<size;i++)
         { for(int j=0;j<size;j++)
             {b[i][j]=0; }
         }
	
}
this->output();

}
void  GRAPH::output()
{
	for(int i=0;i<size;i++)
         {for(int j=0;j<size;j++)
             { cout << arr[i][j]<<"  ";}
             cout <<endl;}
}

void GRAPH:: path_len(char a, char b,int n)
{
	int pos_a;
	int pos_b;
	
	for(int i=0;i<size;i++)
	{   if(arr1[i]==a)
	            pos_a=i;
        if(arr1[i]==b)
	            pos_b=i;
	}
	this->multiplication(n);

	
	cout<<"The no. of path of length "<<n<<"  between  "<<a<<"  and  "<< b<<" is : "<< arr[pos_a][pos_b];
	
	
}

int main()
{
    int num,n , size;
    char ch,a,b;
    
    do{
    	cout<<"enter the number of vertices "<<endl;
         cin>> size;
    	
    GRAPH Dg
    (size); //makking a refrence variable

    Dg.input();// invokes setsize to set tge size if array


    cout<<"\n enter the no.of edges of  graph "<<endl;

    cin>>num;//taking the no. of edge

    Dg.enter(num); //taking input
    cout<<endl;
    
    cout<<"ENTER INITIAL VERTIX "<<endl;
    cin>>a;
     cout<<"ENTER  FINAL VERTIX "<<endl;
    cin>>b;
   
   cout<<"enter the length of path u want to enter"<<endl;
   cin>>n;
    Dg.path_len(a,b,n);
    cout<<"\n\n\n\n";
    
    cout<<setw(80)<<"DO YOU WANT TO CONTINUE ----> (PRESS : Y/y)"<<endl;
    cin>>ch;
    
    cout<<"\n\n";
    }
    while(ch=='y'||ch=='Y') ;
    
}