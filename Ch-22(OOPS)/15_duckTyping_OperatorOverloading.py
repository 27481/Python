# Duck Typing   --> Duck typing is a programming concept that is particularly prominent in dynamically typed languages like Python

# languages that follow duck typing, the type or class of an object is determined by its methods and properties rather than by explicit inheritance or type declarations. If an object supports a particular set of methods or attributes, it is considered to be of a certain type, regardless of its actual class.


class vsCode:
    def execute(self):
        print("complie")
        print("Run")

class MyEditor:
    def execute(self):
        print("spell check")
        print("Conversion check")
        print("compile")
        print("Run")   


class Laptop:
    def code(self, ide):
        print("Coding..")

        ide.execute()
    
       
lap1=Laptop()
ide=MyEditor()

lap1.code(ide)