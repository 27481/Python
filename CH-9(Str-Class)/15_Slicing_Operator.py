#! Slicing Operator 

#! strObject[beg:end:step]     
#* here beggning is inclusive and end is exclusive  and steps are gap between 2 slice 

s1="Mysirg Education Services"
slicing=s1[1:10:2]
print(slicing);

#! Slcing operator works on list as well 

l1=[1,2,3,4,5,6,7,8]
print(l1[4:1:-1])


#! Something equivalent of slicing operator in C++ is sbustring() which is a member function of string class 
""" 

The string class in C++ has a member function called substr, which can be used to extract a substring from a given string. The substr function takes two arguments: the starting position of the substring and the length of the substring to be extracted. Here is an example:



#include <iostream>
#include <string>

int main() {
    std::string myString = "Hello, World!";
    std::string mySubstring = myString.substr(7, 5);
    std::cout << mySubstring << std::endl; // Output: World
    return 0;
}

"""

#! Alternatively, you can use pointers and array indexing to achieve similar functionality to slicing in Python. Here is an example:


""" 
#include <iostream>

int main() {
    int myArray[] = {1, 2, 3, 4, 5};
    int* myPointer = &myArray[1];
    for (int i = 0; i < 3; i++) {
        std::cout << myPointer[i] << std::endl;
    }
    return 0;
}

"""