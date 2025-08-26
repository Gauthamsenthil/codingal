#import necessary packages
from abc import ABC, abstractmethod
#create a base class
class animal(ABC):

    #abstract method
    #should be implemented by all sub-classes
    def move(self):
        passed

# sub class
class human(animal):
    
    def move(self):
        print("i can walk and run")

class snake(animal):

    def move(self):
        print("i can crawl")

class dog(animal):

    def move(self):
        print("i can bark")

class lion(animal):

    def move(self):
        print("i can roar")

#driver code
R = human()
R.move()

K = snake()
K.move()

R = dog()
R.move()

K = lion()
K.move()