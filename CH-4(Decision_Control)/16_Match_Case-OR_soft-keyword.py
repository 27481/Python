# In Python, there is no direct equivalent of the switch statement found in C/C++. Instead, you can use an if-elif-else statement to achieve the same functionality.

#! The match keyword is a new feature that has been introduced in Python 3.10. It provides a way to perform pattern matching on values, similar to how switch works in C/C++.
#! match does not use break; keyword



#* Here's an example of using the match statement in Python:

def match_example(value):
    match value:
        case 1:
            print("Value is 1")
        case 2:
            print("Value is 2")
        case 3 | 4:
            print("Value is 3 or 4")
        case _:
            print("Value is something else")

match_example(1)  # Output: Value is 1
match_example(3)  # Output: Value is 3 or 4
match_example(5)  # Output: Value is something else



"""

In this example, the match statement is used to pattern match on the value parameter passed to the match_example() function. Each case clause specifies a pattern to match, and if the value matches the pattern, the corresponding code block is executed.

The | operator is used to combine multiple patterns, and the _ wildcard pattern matches anything that does not match any of the other patterns.

 """

# So while match can be used to achieve similar functionality to switch in C/C++, it is a new feature in Python and is not a direct equivalent of switch.