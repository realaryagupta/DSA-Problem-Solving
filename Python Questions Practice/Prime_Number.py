# Written by Arya Gupta on 3 March 2024

def prime(num):
    # Check if the number is greater than 1
    if num > 1:
        # Loop through numbers from 2 to half of the given number
        for i in range(2, int(num/2)+1):
            # Check if the number is divisible by any number in the range
            if num % i == 0:
                print("Not Prime")  # If divisible, print that it's not prime
                break  # Exit the loop since the number is not prime
        else:
            print("Prime")  # If the loop completes without finding any divisors, print that it's prime
    else:
        print("Not Prime")  # If the number is less than or equal to 1, it's not prime


# Take input from the user
num = int(input("Enter the number: "))
# Call the prime function to check if the number is prime or not
prime(num)
