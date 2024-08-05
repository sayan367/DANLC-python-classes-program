# Define three numbers
a = 10
b = 20
c = 30

# Find the maximum using ternary if operator
max_num = a if (a > b and a > c) else (b if b > c else c)

# Print the result
print("The maximum number is:", max_num)