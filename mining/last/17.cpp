/*Write a Program to accept a directed graph G and compute the in-degree and out-degree of each vertex. */

#include<iostream>
using namespace std;
class degree{
    private:
    int **a;
	int v;
    public:
    degree(){
        a=NULL;
        v=0;
    }
    degree(int** arr, int size){
    	v=size;
    	a=new int*[size];
    	for(int i=0;i<size;i++){
			a[i]=new int[size];
		}
		a=arr;
	}
    int inDegree(int j){
        int s=0;
        for(int i=0;i<v;i++) s+=a[i][j];
		return s;
	}
    int outDegree(int i){
        int s=0;
        for(int j=0;j<v;j++) s+=a[i][j];
		return s;
	}
	void show(){
        char c='a';
		cout<<"   ";
		for(int i=0;i<v;i++) cout<<char(c+i)<<"  ";
		cout<<endl;
		for(int i=0;i<v;i++){
			cout<<char(c+i)<<"  ";
			for(int j=0;j<v;j++) cout<<a[i][j]<<"  ";
			cout<<endl;
		}
	}
};
int main(){
	int b;
	do{
        int s;
        int** a;
        cout<<"Enter the number of Vertices: ";
        cin>>s;
        char c='a';
        char v1,v2;
        cout<<"\n\nEnter number of edges: ";
        int v;
        cin>>v;
        a=new int* [s];
        for(int i=0;i<s;i++) {
		a[i]=new int[s];}
        for(int i=0;i<s;i++){
            for(int j=0;j<s;j++){
                a[i][j]=0;
            }
        }
        cout<<"The Vertices Names Are: ";
        for(int i=0;i<s;i++) cout<<char(c+i)<<"  ";
        cout<<"\n\n";
        cout<<"\nEnter the elements of array:";
        for(int i=0;i<v;i++){
            cout<<"\nEnter vertex 1 of edge "<<i+1<<" : "; 
            cin>>v1;
            cout<<"\nEnter vertex 2 of edge "<<i+1<<" : "; 
            cin>>v2;
            for(int j=0;j<s;j++){
                if(v1==char(c+j)){
                    for(int k=0;k<s;k++){
                        if(v2==char(c+k)){
                            a[j][k]++;
                        }
                    }
                }
            }cout<<endl;
        }
        degree ob(a,s);
        cout<<"\n\nThe Ajacency matrix is: "<<endl;
        ob.show();
        cout<<"\n\nVertex      in-degree      out-degree"<<endl;
        cout<<endl;
        for(int i=0;i<v;i++){
            cout<<"   "<<char(c+i)<<"             "<<ob.inDegree(i)<<"             "<<ob.outDegree(i)<<endl;
        }
        cout<<"\n\nEnter 1 to continue: ";
        cin>>b;
	}while(b==1);
	return 0;
}
