#a program that returns the largest and smallest elements in a list
#Author: Pedro Mota
#Date: 21/09/2017

def ProblemSheetQ6(numberList):#Write a function that returns the largest and smallest elements in a list.
    biggest=0
    smallest=numberList[0]

    for n in numberList:
        if(smallest<n):
            smallest=n
        elif(n>biggest):
            biggest=n

    return smallest,biggest

def ProblemSheetQ9(n):
	x=20.0
	current=1.0
	next=lambda z: z - ((z*z-x)/2*z)
	while(current!=next):
		current = next(current)
	print current