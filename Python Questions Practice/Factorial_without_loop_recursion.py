# Written by Arya Gupta on 3 March 2024

# Python program to find factorial of a given number

#importing the math function
import math

#Defining the factorial() function to find factorial
def factorial(num):
	return(math.factorial(num))


# Input function to get the number from user
num = int(input('Please enter a number to find the factorial: '))

#Printing the factorial of the given number
print("The factorial of the given number", num, "is",
	factorial(num))