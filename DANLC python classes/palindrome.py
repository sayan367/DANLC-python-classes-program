def is_palindrome(number):
    # Convert the number to a string and check if it reads the same forwards and backwards
    return str(number) == str(number)[::-1]

def find_palindromes(start, end):
    palindromes = []
    for number in range(start, end + 1):
        if is_palindrome(number):
            palindromes.append(number)
    return palindromes

# Get user inputs
start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))

# Find and print the palindromes
palindromes = find_palindromes(start, end)
print(f"Palindromes in the range {start} to {end}: {palindromes}")
