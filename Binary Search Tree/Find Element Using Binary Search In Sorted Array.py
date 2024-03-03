# Written by Arya Gupta on 10 Feb 2024
# Find Element Using Binary Search In Sorted Array.py

# Define the sorted array
arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# Define the binary search function
def binary(arr, x):
    # Initialize the leftmost index of the search range
    left = 0
    # Initialize the rightmost index of the search range
    right = len(arr) - 1
    
    # Continue searching until the left index is less than or equal to the right index
    while left <= right:
        # Calculate the middle index of the search range
        mid = (left + right) // 2
        
        # If the middle element is equal to the target value 'x', return its index
        if arr[mid] == x:
            return mid
        # If the middle element is less than the target value 'x', update the left index to search in the right half
        elif arr[mid] < x:
            left = mid + 1
        # If the middle element is greater than the target value 'x', update the right index to search in the left half
        else:
            right = mid - 1
    
    # If the target value is not found in the array, return -1
    return -1

# Define the target value
x = 30

# Perform binary search to find the index of the target value in the array
result = binary(arr, x)

# If the target value is found in the array, print its index
if result != -1:
    print(f"Element {x} is present at index {result}")
# If the target value is not found in the array, print a message indicating its absence
else:
    print(f"Element {x} is not present in the array")

