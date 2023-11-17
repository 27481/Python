// Program to find the sum of the number given by the user using recursion
#include<iostream>
#include<bits/stdc++.h>


int re(long long int num){
    if(num==1) return 1;
    else{
        long long int s=num+re(num-1);
        return s;
    }
}

using namespace std;
int main(){
    cout<<"Enter the number upto which you want to find the sum:\n";
    long long int num;
    cin>>num;

    cout<<re(num)<<endl;
    return 0;
}