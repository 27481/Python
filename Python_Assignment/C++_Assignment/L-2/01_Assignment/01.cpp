// Take 2 integers input and print the greatest of them

#include<iostream>
#include<bits/stdc++.h>

using namespace std;
int main(){
    int first,second;
    cin>>first>>second;
    first>second?cout<<"The greatest number is"<<first : cout<<"The greatest number is"<<second;
    return 0;
}