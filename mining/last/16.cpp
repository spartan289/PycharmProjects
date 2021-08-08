#include<iostream>
#include<iomanip>

using namespace std;

class complete_graph
{
    private:
            int** arr;
            char* arr1;
            int size;

    public:
           complete_graph();  // default constructor
           void setsize();           //function for set the size of array
           void enter(int num);         // input funtion
           
           bool check(); // check the graph os complete or not
           

}; //class declaration

complete_graph:: complete_graph()
     {
         int** arr=0;
         char* arr1=0;
         int size=0;

     }//default constructur
     void complete_graph:: setsize()
     {
         cout<<"enter the number of vertices "<<endl;
         cin>> size;

         arr1= new char [size];
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


     }// size setting funtion





     void complete_graph::enter(int num)
     {
         char x,y;
         char pos_x;
         int pos_y;
         for(int k=0;k<num;k++)
         {   cout<<endl;
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
                     if(((pos_x==l)&&(pos_y==m))||((pos_y==l)&&(pos_x==m)))
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
     }//input taking funtion



bool complete_graph::check()
{
      int count =0;
      int x = (size*size)-size;
      for(int i=0;i<size;i++)
      {
      	for(int j=0;j<size;j++)
      	{
      		if((i!=j)&&(arr[i][j]==1))
      		{
      			count++;
      		}
      	}
      }
      
      if(count==x)
      return true;
      else
      return false;
} // function to check wheather the graph  is complete or not

int main()
{
    int choice,num;
    char ch;
    complete_graph cg; //makking a refrence variable

    cg.setsize();// invokes setsize to set tge size if array


    cout<<"\n enter the no.of edges of  graph "<<endl;

    cin>>num;//taking the no. of edge

    cg.enter(num); //taking input

if(cg.check()) //check the graph is complete or not
cout<<"\n  \t\t\tTHE GRAPH IS COMPLETE GRAPH"<<endl;
else
cout<<"\n  \t\t\tTHE GRAPH IS NOT A COMPLETE GRAPH"<<endl;
}//main