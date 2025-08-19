#create class
class Point:
    def __init__(self,x = 0,y=0):
        self.x = x
        self.y = y

        #methods to print points in coordinate format
    def __str__(self):
        return "{0},{1}".format(self.x,self.y)

#create an object
p1 = Point(2,3)
print(p1)