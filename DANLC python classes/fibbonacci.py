def fibonacci(n): # defining the function to generate the fibbonaci series 
    if n <= 0: # applying base condition
        return "Invalid input. The input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) # recursive calling of the function fibonacci.
def print_fibonacci_series(n): # print_fibonacci function prints the fibonacci series genreated by fibbonaci function
    if n <= 0:
        print("Invalid input. The input should be a positive integer.")
    else:
        print("Fibonacci Series:")
        for i in range(1, n + 1):
            print(fibonacci(i), end=" ")
# Test the program
n_terms = int(input("Enter the number of terms:"))  # input your value 
print_fibonacci_series(n_terms)