# Written by Arya Gupta on 10 Feb 2024

def bubble(arr):
    n = len(arr)  # Get the length of the array
    for i in range(n):  # Loop through each element of the array
        for j in range(n-i-1):  # Loop through unsorted part of the array
            if arr[j] > arr[j+1]:  # Check if current element is greater than the next one
                # Swap the elements if they are in the wrong order
                arr[j], arr[j+1] = arr[j+1], arr[j]
            
# Example usage
arr = [1, 4, 7, 8, 32, 2, 56, 8, 9, 0, 4]  # Sample array
bubble(arr)  # Sort the array using bubble sort
print(arr)  # Print the sorted array
