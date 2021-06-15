/*
Snakes and Ladders Problem
In this we give nuber of ladders and number of snakes
After the number of ladders, we give the Starting point of the ladder and ending number of ladder;
After the number of snakes, we give the snake head number and the snake tail number.
It will calculate the Minimum number of die numbers to take to reach 100
*/

#include <bits/stdc++.h>

using namespace std;

int main()
{
    int ladders, snakes;
    cout<<"Number of ladders on the board: ";
    cin>>ladders;
    map <int, int> lad;
    map <int, int> snak;
    cout<<"Starting and Ending number of Ladder: \n";
    for(int i=0;i<ladders;i++)
    {
        int u,v;
        cin>>u>>v;
        lad[u]=v;
    }
    cout<<"Number of snakes on the board: ";
    cin>>snakes;
    cout<<"Snake head and Snake Tail number: \n";
    for(int i=0;i<snakes;i++)
    {
        int u,v;
        cin>>u>>v;
        snak[u]=v;
    }
    int moves =0;
    queue <int> q;
    q.push(1);
    bool found = false;
    vector <int> vis(101,0);
    vis[1] = true;
    while(!q.empty() && !found)
    {
        int sz = q.size();
        while(sz--)
        {
            int t = q.front();
            q.pop();
            for(int die=1;die<=6;die++)
            {
                if(t+die==100)
                    found=true;
                if(t+die<=100 && lad[t+die] && !vis[lad[t+die]])
                {
                    vis[lad[t+die]]=true;
                    if(lad[t+die]==100)
                        found=true;
                    q.push(lad[t+die]);
                }
                else if(t+die<=100 && snak[t+die] && !vis[snak[t+die]])
                {
                    vis[snak[t+die]]=true;
                    if(snak[t+die]==100)
                        found=true;
                    q.push(snak[t+die]);
                }
                else if(t+die<=100 && !vis[t+die] && !snak[t+die] && !lad[t+die])
                {
                    vis[t+die]=true;
                    q.push(t+die);
                }
            }
        }
        moves++;
    }
    if(found)
        cout<<"Minimum number of steps to reach 100: "<<moves;
    else
        cout<<-1;
    return 0;
}

/*
Output: 
Ladders - 8
Ladders Starting and ending number - 
U = 1    V = 38
U = 4    V = 14
U = 9    V = 31
U = 21   V = 42 
U = 28   V = 84
U = 51   V = 67
U = 72   V = 91
U = 80   V = 99
Snake head and snake tail number - 
U = 98   V = 79
U = 95   V = 75
U = 92   V = 73
U = 87   V = 36
U = 62   V = 19
U = 64   V = 60
U = 17   V = 7
U = 54   V = 34

Minimun number of steps to reach 100 : 7
*/