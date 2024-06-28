# Written by Arya Gupta on 3 March 2024
# Check If The Elements Of An Array Are Consecutive

# Driver Code
arr = [9, 2, 7, 12, 11, 4, 5, 6, 8, 3, 1, 14, 19, 13, 10]

def check_consecutive(arr):
    consecutive_elements = []
    for i in range(len(arr)-1):
        if arr[i+1] - arr[i] == 1:
            consecutive_elements.append((arr[i], arr[i+1]))
    return consecutive_elements

consecutive_pairs = check_consecutive(arr)
if consecutive_pairs:
    print("Consecutive elements:")
    for pair in consecutive_pairs:
        print(pair)
else:
    print("No consecutive elements found.")
