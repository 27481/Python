#include <iostream>

using namespace std;

long long sum(int start, int end) {
    if (start == end) {
        return start;
    }
    else {
        int mid = (start + end) / 2;
        long long left_sum = sum(start, mid);
        long long right_sum = sum(mid + 1, end);
        return left_sum + right_sum;
    }
}

int main() {
    
    int n;
    cout<<"Enter the number upto which you want to find the sum of the n terms:\n";
    cin>>n;
    long long int result = sum(1, n);
    cout << "The sum of the first " << n << " numbers is: " << result << endl;
    return 0;
}
