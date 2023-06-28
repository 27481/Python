/* 
Yes, in addition to accessing member variables, the dot operator can also be used to access member functions and to add or modify object attributes in both C++ and Python.

In C++, you can use the dot operator to call member functions of an object, and to access or modify its member variables, like this:
*/
#include <iostream>
#include <string>
using namespace std;

class Person {
public:
    string name;
    int age;

    void say_hello() {
        cout << "Hello, my name is " << name << " and I'm " << age << " years old." << endl;
    }
};

int main() {
    Person person;
    person.name = "John";
    person.age = 30;

    // Call the "say_hello" method using the dot operator
    person.say_hello();  // Output: "Hello, my name is John and I'm 30 years old."

    // Access or modify the "name" member variable using the dot operator
    cout << person.name << endl;   // Output: "John"
    person.name = "Mary";
    cout << person.name << endl;   // Output: "Mary"

    return 0;
}

