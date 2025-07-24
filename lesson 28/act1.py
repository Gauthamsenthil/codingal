class IOstring():
    
    
    #constructor to set default values
    def __init__(self):
        self.str1 = ""

    #function to get input from user
    def get_string(self):
        self.str1 = input("enter string : ")
    
    
    #function to print the string in upper case
    def print_String(self):
        print("Result is :", self.str1.upper())

#object creation
str1 = IOstring()

#call funtion
str1.get_string()
str1.print_String()