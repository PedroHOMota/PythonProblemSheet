#A function that returns the largest and smallest elements in a list
#Author: Pedro Mota
#Date: 21/09/2017

def ProblemSheetQ6(numberList):
    biggest=0
    smallest=numberList[0]

    for n in numberList:
        if(smallest<n):
            smallest=n
        elif(n>biggest):
            biggest=n

    return smallest,biggest

