#A function to reverse a string.
#Author: Pedro Mota
#Date: 21/09/2017
         
def ProblemSheetQ10(string): 
    reversed=""

    for n in range(len(string)-1,-1,-1): #Loop from end of the string to the beginning 
        reversed+=string[n]				 #Concantenate the chars togehter

    return reversed

