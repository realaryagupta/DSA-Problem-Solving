# Wrote by Arya Gupta on 10 Feb 2024

def selection_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Assume the current element is the minimum
        min_index = i
        
        # Traverse the unsorted part of the array
        for j in range(i+1, n):
            # If any element is smaller than the assumed minimum, update the minimum index
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the minimum element with the current element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
selection_sort(arr)
print("Sorted array:", arr)