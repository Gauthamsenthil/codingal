#create class
class pair_elements:
    

    def twoSum(self,nms,target):
        #create an dictionary
        lookup = {}

        #Iterate through the tuple
        for i, num in enumerate(nms):
            if target - num in lookup:
                return(lookup[target - num], i)
            lookup[num] = i

#take input of dum from the user
value = int(input("enter sum for which you want to make this search :"))
print("index1 = %d, index2 = %d"%pair_elements().twoSum((10,20,30,40,50,60,70), value))