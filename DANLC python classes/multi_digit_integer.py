"""Write a program that inputs a multi digit integer 
from the user and prints the sum of all its even digits.

Example : Input :2467
Output : 12"""


def sum_even_digits(number):
    # Convert the number to a string to iterate over each digit
    number_str = str(number)
    total_sum = 0
    
    # Iterate over each character in the string
    for char in number_str:
        # Convert the character back to an integer
        digit = int(char)
        
        # Check if the digit is even
        if digit % 2 == 0:
            total_sum += digit
    
    return total_sum

# Input from user
user_input=str(input("Enter the non negetive integer:-"))
print(sum_even_digits(user_input))# calling and printing the result at same time.2467
