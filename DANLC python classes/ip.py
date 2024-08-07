import re

def is_valid_ip(ip_address):
    # Define the regular expression pattern for a valid IP address
    pattern = r'^((25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'
    
    # Use the pattern to match the IP address
    if re.match(pattern, ip_address):
        return True
    return False

# Test cases
print(is_valid_ip("12.22.212.52"))  # True
print(is_valid_ip("12.23.49"))      # False
print(is_valid_ip("12.42,49,233"))  # False
print(is_valid_ip("22.22.292.42"))  # False