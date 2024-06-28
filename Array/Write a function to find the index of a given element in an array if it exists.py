# Write a function to find the index of a given element in an array (if it exists).

def find_element_index(arr, num):
    for i in range(len(arr)):
        if num == arr[i]:
            return i
    return -1  # Return -1 if element not found

arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 654]
num = int(input("Enter the Number Whose Index you want to Find: "))

index = find_element_index(arr, num)

if index != -1:
    print(f"The Index of {num} is {index}")
else:
    print("Index Not Found")