# Function to get user input (for testing purposes)
def get_user_input():
    # Simulate user input with a predefined list of integers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    return numbers

# Function to separate even and odd integers
def separate_even_odd(numbers):
    even_integers = []
    odd_integers = []
    for number in numbers:
        if number % 2 == 0:
            even_integers.append(number)
        else:
            odd_integers.append(number)
    return even_integers, odd_integers

# Main function
def main():
    numbers = get_user_input()
    even_integers, odd_integers = separate_even_odd(numbers)
    
    print("Even integers are:", ' '.join(map(str, even_integers)))
    print("Odd integers are:", ' '.join(map(str, odd_integers)))

# Execute the program

print(main())