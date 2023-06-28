#include<iostream>
#include<bits/stdc++.h>
using namespace std;

int main(){
    int radius;
    cout<<"Enter the radius of the circle whose area you want to find out:\n";
    cin>>radius;
    float circumference=2*3.14*radius, area=3.14*radius*radius;
    circumference>radius?cout<<"Larger one is:\n"<<circumference:cout<<"Larger one is:\n"<<radius;
    return 0;
}
