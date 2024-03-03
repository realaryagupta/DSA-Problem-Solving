# Written by Arya Gupta on 3 March 2024
# How do you find the largest and smallest number in an unsorted integer array?

def find_largest(arr):
    """
    Finds the largest number in the unsorted integer array.
    
    Parameters:
        arr (list): Input list of integers.
    """
    largest = float('-inf')  # Initialize largest to negative infinity
    for num in arr:
        if num > largest:
            largest = num
    print("Largest number:", largest)

def find_smallest(arr):
    """
    Finds the smallest number in the unsorted integer array.
    
    Parameters:
        arr (list): Input list of integers.
    """
    smallest = float('inf')  # Initialize smallest to positive infinity
    for num in arr:
        if num < smallest:
            smallest = num
    print("Smallest number:", smallest)

# Driver Code
arr = [4, 9, 3, 7, 1, 6, 4, 5, 9, 2, 10, 4, 7, 3, 6, 8, 5, 8, 2, 10]
find_largest(arr)
find_smallest(arr)
