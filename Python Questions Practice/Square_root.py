# Written by Arya Gupta on 3 March 2024

# Write a Python program to calculate the square root of a given number.

def sqrt(num):
    if num < 0:
        print("Square root is not defined for negative numbers.")
    else:
        for i in range(int(num ** 0.5) + 1):  # Iterate up to the square root of num
            if i * i == num:
                print(f"Square root of {num} is {i}")
                break
        else:  # This block executes only if the loop completes without encountering a break
            print(f"{num} is not a perfect square.")

num = int(input("Enter the number: "))
sqrt(num)
