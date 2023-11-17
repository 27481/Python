# adding extra functionality to a function by using decorator2 function 


def decor_result(result_func):
    def distinction(marks):
        for m in marks:
            if(m>=75):
                print("Distinction")
        else:
            result_func(marks)
    return distinction


@decor_result
def result(marks):
    for m in marks:
        if(m>33):
            pass
        else:
            print("Fail")
            break
    else:
        print("Pass")


result([55,66,70,45,80])