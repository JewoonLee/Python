#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int n, curd=0, totald=0, sum=0;
    cin>>n;

    int *price = new int[n];
    int *dist = new int[n-1];
    
    
    for(int i=0;i<n-1;i++){
        cin>>dist[i]; 
        totald+=dist[i];
    }
    for(int i=0;i<n;i++){
        cin>>price[i];
    }

    int idx=0;
    while(curd<totald)
    {
        int i, pred=curd;
        for(i=idx;i<n && price[idx]<=price[i] && curd<totald;curd+=dist[i], i++){
            if(i == n-1){

                break;
            }
        }
        sum+=price[idx]*(curd-pred);
        idx=i;
    }
    cout<<curd<<endl;
    cout<<totald<<endl;
    cout<<sum<<endl;
    return 0;
}