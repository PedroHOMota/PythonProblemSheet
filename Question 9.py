#Function to calculate square root using Newton's method
#Author: Pedro Mota
#Date: 21/09/2017
         
def ProblemSheetQ9(n):
    z=1.0

    while True :
        z_next = z - ((z*z - n) / (2 * z))
        if z_next == z:
            return z_next
        z=z_next


