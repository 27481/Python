// using iterative approach to find the sum upto n number given by the user 

#include<iostream>
#include<bits/stdc++.h>
using namespace std;

int main(){
    long long int num;
    cout<<"Enter the number upto which you want to print the sum:\n";
    cin>>num;

    long long int sum=0;

    for(int i=1; i<num; i++){
        sum+=i;
    }
    cout<<sum<<endl;
    return 0;
}