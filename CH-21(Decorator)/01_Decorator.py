# Decorator 

""" 
The job of decorator is to modify the functionality of a method
"""

#! input function ----->>decorator---->>> output function with modified functionality


def result(marks):
    for m in marks:
        if m>33:
            pass
        else:
            print("Fail")
            break
    else:
        print("Pass")



def decor_result(result_func): #! defining a decorator and giving it res() as argument
    def distinction(marks):
        for m in marks:
            if m>=75:
                print("Distinction")
        else:
            result_func(marks)
    return distinction