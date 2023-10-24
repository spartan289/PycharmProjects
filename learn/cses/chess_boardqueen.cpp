#include <bits/stdc++.h>

using namespace std;
void placequeen(char arr[][8], int x, int y)
{
    for (int i = 0; i < 8; i++)
    {
        arr[x][i] = '*';
        arr[i][y] = '*';
    }
    int i = x, j = y;
    while (i >= 0 && j >= 0)
    {
        arr[i][j] = '*';
        i--;
        j--;
    }
    i = x, j = y;
    while (i < 8 && j < 8)
    {
        arr[i][j] = '*';
        i++;
        j++;
    }
    i = x, j = y;
    while (i >= 0 && j < 8)
    {
        arr[i][j] = '*';
        i--;
        j++;
    }
    i = x, j = y;
    while (i < 8 && j >= 0)
    {
        arr[i][j] = '*';
        i++;
        j--;
    }
    arr[x][y] = 'Q';
}
int c = 0;
void possbileconfig(char arr[][8], int j)
{
    if (j == 8)
    {
        c++;
        return;
    }
    else
    {
        for (int i = 0; i < 8; i++)
        {
            if (arr[j][i] == '.')
            {
                char b[8][8];
                memcpy(b, arr, 8 * 8 * sizeof(char));
                placequeen(b, j, i);
                possbileconfig(b, j + 1);
            }
        }
        return;
    }
}
void print_queen(char arr[][8])
{
    for (int i = 0; i < 8; i++)
    {
        /* code */
        for (int j = 0; j < 8; j++)
        {
            /* code */
            cout << arr[i][j] << " ";
        }
    }
}
int main()
{
    char arr[8][8];
    int i, j;
    for (i = 0; i < 8; i++)
    {
        for (j = 0; j < 8; j++)
        {
            cin >> arr[i][j];
        }
    }
    possbileconfig(arr, 0);
    cout << c;
}
/*
........
........
..*.....
........
........
.....**.
...*....
........
*/
