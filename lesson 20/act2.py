import random #import module
import time
def getRandomDate(startDate , endDate): #defining function
    print("Printing random date between", StartDate, "and", endDate)
    randomGenerator = random.random()
    dateFormat = '%m/%d/%y'
    startTime = time.mktime(time.strptime(startDate,dateFormat))
    endTime = time.mktime(time.strptime(endDate,dateFormat))

    randomTime = starttime + randomGenerator * (endTime - startTime)
    randomDate = time.strftime(dateformat,time.localtime(randomTime))
    return randomDate
    #display result
print("random date = ", getRandomDate("1/1/2016","12/12/2018"))
