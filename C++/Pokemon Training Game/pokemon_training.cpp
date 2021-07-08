// Pokemon Training

#include<bits/stdc++.h>
using namespace std;
int main()
{
	int n;
	cout<<"Enter the size of powers of pokemon array:";
	cin>>n;
	int arr[n];
	int maxi=0,mini=0;
	for(int i=0;i<n;i++)
	{
		cin>>arr[i];
	}
	for(int i=0;i<n;i++)
	{
		if(mini==0 && maxi==0)
		{
			mini=arr[0];
			maxi=arr[0];
			cout<<mini<<" "<<maxi<<endl;
		}
		else
		{
			mini=min(mini,arr[i]);
			maxi=max(maxi,arr[i]);
			cout<<mini<<" "<<maxi<<endl;
		}
	}
	return 0;
}
