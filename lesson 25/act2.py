#zip element of two lists
s1 = {2,3,1}
s2 = {'a','b','c'}
s3 = list(zip(s1,s2))
print(s3,"\n")

# zip element of two lists
#print elements one by one, but element of 2nd list will be in reverse order
list1 = [10,20,30,40]
list2 = [100,200,300,400]
for x,y in zip(list1, list2[::-1]):
    print(x,y)

#zip into dictionary
stock = ['reliance','infosys','tcs']
prices = [2175,1127,1750]

new_dict = {stock: prices for stock,prices in zip(stock,prices)}
print('\n{}'.format(new_dict))