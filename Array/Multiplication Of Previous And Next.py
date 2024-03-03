# Written by Arya Gupta on 3 March 2024
# Multiplication Of Previous And Next

def add(arr):
    """
    Adds each element with its adjacent element in the array.
    
    Parameters:
        arr (list): Input list of integers.
    
    Returns:
        list: New list containing the sum of each element with its adjacent element.
    """
    new_arr = []
    for i in range(len(arr)-1):
        # Calculate the sum of current element and its adjacent element
        a = arr[i] + arr[i+1]
        # Append the sum to the new_arr list
        new_arr.append(a)
    else:
        # Print the new_arr list when the loop completes
        print(new_arr)


# Driver Code
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
add(arr)
