#include <iostream>
typedef unsigned long long int ll;
using namespace std;

// Function with default arguments
void display(int a = 10, int b, int c = 20) {
    cout<<"a:"<<a<<",b:"<<b<<",c:"<<c<<endl;
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // Calling the function without providing all arguments
    display(5);           // Output: a: 5, b: 10, c: 20
    display(5, 15);       // Output: a: 5, b: 15, c: 20
    display(5, 15, 25);   // Output: a: 5, b: 15, c: 25
    


          
 
    return 0;
}