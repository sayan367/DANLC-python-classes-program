def process_state_capital_pairs(input_line):
    # Split the input line by '-' to get each state-capital pair
    pairs = input_line.split('-')
    
    # Iterate through each pair
    for pair in pairs:
        # Split each pair by '||' to separate state and capital
        state, capital = pair.split('||')
        # Print the capital
        print(capital)


input_line = input("Enter the state-capital pairs: ")
process_state_capital_pairs(input_line)