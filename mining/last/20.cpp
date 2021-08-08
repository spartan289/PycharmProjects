#include <bits/stdc++.h>
using namespace std;
 
// Function to calculate
// leaf nodes in m_arry-ary tree
int calcNodes(int m_arry, int nodes)
{
    int result = 0;
 
    result = nodes * (m_arry - 1) + 1;
 
    return result;
}
 
// Driver code
int main()
{
    int m_arry, nodes;
    cout << "\n\nEnter the value of m-ary tree: ";
    cin >> m_arry;

    cout << "\nEnter the value of nodes: ";
    cin >> nodes;

    cout << "\nThe number of leaf nodes in the tree = " << calcNodes( m_arry, nodes) << endl << endl;
 
    return 0;
}