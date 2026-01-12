#include <bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{
  ios::sync_with_stdio(0);
  cin.tie(0);

  int n;
  cin>>n;
  vector<int>v(n);
  for(int i=0;i<n;i++)cin>>v[i];
  int mn=INT_MAX,idx=-1;
  for(int i=0;i<n;i++){
    if(mn>v[i]){
        mn=v[i];
        idx=i+1;
    }
    if(mn!=v[i]){
        for(int j=i-1;j>=0;j--){
            if(v[j]<v[i]){cout<<j+1<<" ";break;}
        }
    }else cout<<0<<" ";
    
}
cout<<endl; 

    return 0;
}