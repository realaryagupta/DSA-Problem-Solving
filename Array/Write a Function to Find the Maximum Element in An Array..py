# Written by Arya Gupta on 11 March 2024
# Write a Function to Find the Maximum Element in An Array.

def max(arr):
    pointer = 0
    for i in range(len(arr)):
        if arr[i] > pointer:
            pointer = arr[i]
    print(pointer)

# Driver Code
arr = [1,2,54,3,6,11,4,23,56,7,43,5]
max(arr)
