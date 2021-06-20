#include<bits/stdc++.h>
using namespace std;

int main()
{
    int i,j,k;
    string s,t;
    int key;
    cout<<"Enter the key\n";
    cin>>key;
    
    cout<<"Enter the message\n";
    cin>>s;
    
    for(i=0;i<s.size();i++)
    {   
        if(s[i]>='A'&&s[i]<='Z')
        t+=(s[i]-'A'-key)%26+'A';
        else
        t+=(s[i]-'a'-key)%26+'a';
        
    }
    cout<<"\nDecrypted message is "<<t<<'\n';
    return 0;
}