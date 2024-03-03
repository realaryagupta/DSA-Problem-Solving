# Written by Arya Gupta on 3 March 2023
# How do you find the missing number in a given integer array of 1 to 100?
import random

def find_missing_number(arr):
    """
    Finds the missing number in a given integer array of 1 to 100.
    
    Parameters:
        arr (list): Input list of integers.
    
    Returns:
        int: The missing number.
    """
    expected_sum = sum(range(1, 101))  # Sum of integers from 1 to 100
    actual_sum = sum(arr)  # Sum of elements in the given array
    missing_number = expected_sum - actual_sum
    return missing_number

# Driver Code
arr = list(range(1, 101))
# Removing a Random Index so we can later find it which it was 
random_index = random.randint(0, 99)
missing_number = arr.pop(random_index)
print("Removed:", missing_number)
print("Original array:", arr)

result = find_missing_number(arr)
print("Missing number:", result)
