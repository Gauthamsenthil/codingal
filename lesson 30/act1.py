#class creation
class myClass:

    #private variable
    __privatevar = 27;

    #private method
    def __privMeth(self):
        print("I'm inside class myClass")

    #function to print values of private variable
    def hello(self):
        print("private variable value:",myClass.__privatevar)

#object creation and method call
foo = myClass()
foo.hello()
foo.__privMeth