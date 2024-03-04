# Written By Arya Gupta on 4 March 2024
# Write a Program to check whether a string is a valid shuffle of two strings or not

# Driver Code
# Driver Code
string =  "A man, a plan, a canal, Panama"

# Removing spaces and commas and converting to lowercase
str_without_spaces_and_commas = string.replace(" ", "").replace(",", "").lower()

# Function to check for palindrome
def palindrome(str):
    for i in range(len(str) // 2):  # Loop only till half of the string
        if str[i] != str[len(str) - i - 1]:  # Compare characters from both ends
            print("Not a Palindrome")
            return
    print("Palindrome")

palindrome(str_without_spaces_and_commas)
