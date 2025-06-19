L = [4, 5, 1, 2, 9, 7, 10, 8]
print("original list : ",L)

# variables to store the sum of
# the list
count = 0

#finding the sum
for i in L:
    count += i

#divide the total elements by number of elements
avg = count/len(L)

print("sum = ", count)
print("average = ", avg)

#sorting the elements of the list
L.sort()

#printing the first elements
print("first elements is:",L[0])

#printing the last elements
print("last element is: ", L[-1])