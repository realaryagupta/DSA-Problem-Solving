## Palindrome Question
# Write a function that checks if a given string is a palindrome (reads the same forwards and backwards).

# Prompt the user to enter a text to check for palindrome
txt = input("Enter the text you want to check: ")

# Convert the text to lowercase to ensure the check is case-insensitive
txt = txt.lower()

# Convert the string into a list of characters
txt_str = list(txt)

# Initialize a flag to assume the text is a palindrome
is_palindrome = True

# Iterate through the first half of the list
for i in range(len(txt_str) // 2):
    # Compare characters from the start and end moving towards the center
    if txt_str[i] != txt_str[-(i + 1)]:
        # If any characters do not match, set the flag to False
        is_palindrome = False
        # Break out of the loop as we have determined it is not a palindrome
        break

# Check the flag and print the appropriate message
if is_palindrome:
    print("The String is a Palindrome")
else:
    print("The String is not a Palindrome")
