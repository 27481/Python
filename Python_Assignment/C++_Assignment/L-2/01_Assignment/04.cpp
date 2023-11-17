// Given the length and breadth of a rectangle, write a program to find whether numerically the area of
// the rectangle is greater than its perimeter.

#include<iostream>
#include<bits/stdc++.h>
using namespace std;

int main(){
    int length, breadth;
    cout<<"Enter the length and breadth of the rectangle respectively:\n";
    cin>>length>>breadth;

    float perimeter=2*(length+breadth), area=length*breadth;
    //!Using Terinary Operator 
    (perimeter>area) ? cout<<"Perimeter is greater than area":cout<<"Area is greater than perimeter";
    return 0;
}