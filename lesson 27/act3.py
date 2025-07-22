#create parrot 
class parrot:

    #class attribute
    species = "bird"

    #instance attribute
    def __init__(self,name,age):
        self.name = name
        self.age = age
#instantiate the parrot class
blu = parrot("blu",10)
woo = parrot("woo",15)

#access the class attribute
print("blu is a {}".format(blu.species))
print("woo is a {}".format(woo.species))

#to access the instant attribute
print("{} is {} years old".format(blu.name,blu.age))
print("{} is {} years old".format(woo.name,woo.age))