#A function that merges two sorted lists into a new sorted list
#Author: Pedro Mota
#Date: 21/09/2017
         
def ProblemSheetQ8(list1,list2):
    list1+=list2 #Concatanete the two list together
    list1.sort() #Sort the new list
    return list1


