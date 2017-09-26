#A program that prints the factorial of a number
#Author: Pedro Mota
#Date: 21/09/2017
         
def ProblemSheetQ4(n):
    print("\nAnswe to Q3:")
    factorial=1
    sum=0
    for i in range(2,n):
        factorial*=i

    for i in enumerate(factorial):
        sum+=i

    print(sum)

def ProblemSheetQ5(): #guessing game
    guesses=[]
    n=random.randint(0,100)
    print("\nAnswe to Q4:")
    print("Guess the number")
    

    while (True):
        guess= int(input("Enter a number:"))
        if(guesses.__contains__(guess)):
            print("You have tried this number already")
            continue
        elif(n==guess):
            print("Você acertou!!!! Number of tries "+str(guesses.count))
            break
        else:
            if(guess<n):
                print("Number too small")
            elif(guess>n):
                print("Number big small")
            guesses.__add__(guess)

def ProblemSheetQ6(numberList):#Write a function that returns the largest and smallest elements in a list.
    biggest=0
    smallest=numberList[0]

    for n in numberList:
        if(smallest<n):
            smallest=n
        elif(n>biggest):
            biggest=n

    return smallest,biggest

def ProblemSheetQ7(palindrome): #Write a function that tests whether a string is a palindrome.
    if(palindrome==palindrome[::-1]):
        return True
    else:
        return False
    
def ProblemSheetQ8(list1,list2): #Write a function that merges two sorted lists into a new sorted list. [1,4,6],[2,3,5] → [1,2,3,4,5,6].
    list1+=list2
    list1.sort()
    return list1

def ProblemSheetQ9(n):

def ProblemSheetQ10(string): #Write a function to reverse a string.
    reversed=""

    for n in range(len(string)-1,-1,-1):
        reversed+=string[n]

    return reversed

ProblemSheetQ1()
ProblemSheetQ2()
ProblemSheetQ3()
print(ProblemSheetQ7("ana"))