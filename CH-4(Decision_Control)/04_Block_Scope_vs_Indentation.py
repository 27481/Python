""" 
In C++, block scope is determined by enclosing braces {}. Any variable declared within a block is only accessible within that block and its sub-blocks. 

For example:

int main() 
{
    int x = 5;
    {
        int y = 10;
        cout << x + y << endl; // Accessible, outputs 15
    }
    cout << x + y << endl; // Not accessible, causes an error
    return 0;
}
"""





""" In this example, x is declared in the main block and is accessible within the sub-block that declares y. However, y is not accessible outside of its block.

In Python, block scope is determined by the indentation level. Any code that is indented to the same level is considered to be within the same block. For example: """
#! make a standard of giving 4 space if you are trying to make an indentation block

def main():
    x = 5
    if x > 0:
      y = 10
      print(x + y)  # Accessible, outputs 15
    print(x + y)  # Not accessible, causes an error

main()


""" 
In both C++ and Python, block scope and indentation are used to control the visibility and accessibility of variables within a program. However, the syntax and rules for determining block scope are different between the two languages.
"""
