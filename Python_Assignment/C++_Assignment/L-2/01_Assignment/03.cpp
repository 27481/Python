// Any year is input through the keyboard. Write a program to determine whether the year is a leap year
// or not. (Considering leap year occurs after every 4 years)
#include<iostream>
#include<bits/stdc++.h>
using namespace std;

bool leapYear(int y){
    if(y%400==0)
      return true;
    if(y%100==0)
      return false;
    if(y%4==0)
      return true;
    return false;
}
int main(){
    int year;
    cout<<"Enter the year which you want to check is leap year or not :\n";
    cin>>year;

    cout<<(bool)(leapYear(year))<<endl;
    return 0;
}